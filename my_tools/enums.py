from enum import Enum


class DialogManagerKeys(str, Enum):

    BOT = "bot"
    CONFIG = "config"
    EVENT_FROM_USER = "event_from_user"
    TRANSLATOR_HUB = "_translator_hub"
    FILTERS = "filters"


class DateTimeKeys(str, Enum):

    DEFAULT = "default"
    NOW = "now"
    NOW_ZERO = "now_zero"
    TODAY = "today"


class Langs(str, Enum):
    af = "🇿🇦"  # Afrikaans
    ar = "🇸🇦"  # Arabic
    az = "🇦🇿"  # Azerbaijani
    be = "🇧🇾"  # Belarusian
    bg = "🇧🇬"  # Bulgarian
    bn = "🇧🇩"  # Bengali
    bs = "🇧🇦"  # Bosnian
    ca = "🇪🇸"  # Catalan
    cs = "🇨🇿"  # Czech
    da = "🇩🇰"  # Danish
    de = "🇩🇪"  # German
    el = "🇬🇷"  # Greek
    en = "🇬🇧"  # English
    es = "🇪🇸"  # Spanish
    et = "🇪🇪"  # Estonian
    fa = "🇮🇷"  # Persian
    fi = "🇫🇮"  # Finnish
    fr = "🇫🇷"  # French
    he = "🇮🇱"  # Hebrew
    hi = "🇮🇳"  # Hindi
    hr = "🇭🇷"  # Croatian
    hu = "🇭🇺"  # Hungarian
    hy = "🇦🇲"  # Armenian
    id = "🇮🇩"  # Indonesian
    it = "🇮🇹"  # Italian
    ja = "🇯🇵"  # Japanese
    ka = "🇬🇪"  # Georgian
    kk = "🇰🇿"  # Kazakh
    km = "🇰🇭"  # Khmer
    ko = "🇰🇷"  # Korean
    ky = "🇰🇬"  # Kyrgyz
    lt = "🇱🇹"  # Lithuanian
    lv = "🇱🇻"  # Latvian
    mk = "🇲🇰"  # Macedonian
    mn = "🇲🇳"  # Mongolian
    ms = "🇲🇾"  # Malay
    my = "🇲🇲"  # Burmese
    nb = "🇳🇴"  # Norwegian Bokmål
    nl = "🇳🇱"  # Dutch
    pl = "🇵🇱"  # Polish
    pt = "🇵🇹"  # Portuguese
    ro = "🇷🇴"  # Romanian
    ru = "🇷🇺"  # Russian
    sk = "🇸🇰"  # Slovak
    sl = "🇸🇮"  # Slovenian
    sq = "🇦🇱"  # Albanian
    sr = "🇷🇸"  # Serbian
    sv = "🇸🇪"  # Swedish
    sw = "🇹🇿"  # Swahili
    ta = "🇱🇰"  # Tamil
    th = "🇹🇭"  # Thai
    tr = "🇹🇷"  # Turkish
    uk = "🇺🇦"  # Ukrainian
    uz = "🇺🇿"  # Uzbek
    vi = "🇻🇳"  # Vietnamese
    zh = "🇨🇳"  # Chinese