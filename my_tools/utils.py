from datetime import datetime
import pytz

from .enums import DateTimeKeys


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
            # datetime.datetime(2025, 3, 5, 11, 49, 56, 699557)
            return now.replace(microsecond=0)

        case DateTimeKeys.NOW_ZERO:
            return now.replace(minute=0, second=0, microsecond=0)
        

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