from datetime import datetime, timedelta
import pytz
import json

from aiogram.fsm.storage.redis import RedisStorage

from .enums import DateTimeKeys
from .globals import NUMS
from .custon_types import MetricData


def get_datetime_now(
        date_time_key: DateTimeKeys = DateTimeKeys.DEFAULT,
        custom_date: datetime | None = None,
        time_zone: str = "Asia/Nicosia"
        ) -> str | datetime:

    tz = pytz.timezone(time_zone)
    now: datetime = custom_date or datetime.now(tz=tz).replace(tzinfo=None)

    match date_time_key:

        case DateTimeKeys.DEFAULT:
            # str: 2025-03-05T11:49:35
            return now.isoformat(timespec="seconds")
        
        case DateTimeKeys.NOW:
            # datetime.datetime(2025, 3, 5, 11, 49, 56, 0)
            return now.replace(microsecond=0)

        case DateTimeKeys.NOW_ZERO:
            # datetime.datetime(2025, 3, 19, 15, 0)
            return now.replace(minute=0, second=0, microsecond=0)
        
        case DateTimeKeys.TODAY:
            # datetime.datetime(2025, 3, 19, 0, 0)
            return now.replace(hour=0, minute=0, second=0, microsecond=0)
        

def get_time_delta(time: str) -> str:
    """
    Calculate the difference between two datetime strings and return it in the most suitable unit.
    
    Parameters:
    - time1: str -> First datetime in ISO format (YYYY-MM-DDTHH:MM:SS)
    - time2: str -> Second datetime in ISO format (YYYY-MM-DDTHH:MM:SS)
    
    Returns:
    - str -> Time difference with an appropriate unit (seconds, minutes, or hours).
    """
    # Convert strings to datetime objects
    dt2 = datetime.fromisoformat(get_datetime_now())
    dt1 = datetime.fromisoformat(time)
    
    # Calculate time difference in seconds
    diff = abs((dt2 - dt1).total_seconds())

    # Choose the best unit
    if diff < 60:
        return f"{diff:.0f}s"
    elif diff < 3600:
        return f"{diff / 60:.1f}m"
    else:
        return f"{diff / 3600:.0f}h"
    

def format_counter(num: int) -> str:

    if not isinstance(num, int) or num < 0:
        raise TypeError("Input number not int or number < 0")
    
    num = str(num)

    if len(num) == 1:
        num = "0" + num

    return ''.join([NUMS[n] for n in list(num)])


async def calc_active_users_metrics(
        users_storage: RedisStorage, 
        users: list[str]
        ) -> tuple[int, int, int]:

    today: datetime = get_datetime_now(DateTimeKeys.TODAY)

    dau_threshold = today  # activity today counts as DAU
    wau_threshold = today - timedelta(days=7)
    mau_threshold = today - timedelta(days=30)

    dau = 0
    wau = 0
    mau = 0

    for user in users:

        user_data = await users_storage.redis.lrange(f"{user}_a", 0, -1)

        # Flags for this user whether they've been counted for each metric
        active_dau = False
        active_wau = False
        active_mau = False

        for ud in user_data:

            data = json.loads(ud)

            if data.get("date"):
                user_time = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S')

                # Update flags if thresholds are met
                if not active_dau and user_time >= dau_threshold:
                    active_dau = True
                if not active_wau and user_time >= wau_threshold:
                    active_wau = True
                if not active_mau and user_time >= mau_threshold:
                    active_mau = True

                # If the user qualifies for all metrics, no need to scan further records
                if active_dau and active_wau and active_mau:
                    break

        # Count the user if any of the metrics was met
        if active_dau:
            dau += 1
        if active_wau:
            wau += 1
        if active_mau:
            mau += 1

    return dau, wau, mau


async def get_users(db: RedisStorage, admins: list[int]) -> list[int]:
    
    users = []
    async for user in db.redis.sscan_iter("known_users"):
        # Decode bytes to string, if needed
        if isinstance(user, bytes):
            user = user.decode("utf-8")

        if user not in admins:
            users.append(user)
    return users


async def calc_mertics(db: RedisStorage, admins: list[int]) -> MetricData:

    users: list[int] = await get_users(db, admins)

    dau, wau, mau = await calc_active_users_metrics(db, users)

    stickness: int = int(round(dau / mau, 2)*100) if mau > 0 else 0

    return MetricData(
        users=len(users),
        dau=dau,
        wau=wau,
        mau=mau,
        stickness=stickness
    )