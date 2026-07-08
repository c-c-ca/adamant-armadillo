from datetime import datetime
from typing import Final
from zoneinfo import ZoneInfo

import pytest

from adamant_armadillo_core import get_noon_on_same_day

TZ: Final[str] = "America/New_York"

YEAR = 2026
MONTH = 5
DAY = 10

NOON: Final[datetime] = datetime(
    year=YEAR,
    month=MONTH,
    day=DAY,
    hour=12,
    minute=0,
    second=0,
    microsecond=0,
    tzinfo=ZoneInfo(TZ),
)

START_OF_DAY: Final[datetime] = datetime(
    year=YEAR,
    month=MONTH,
    day=DAY,
    hour=12,
    minute=0,
    second=0,
    microsecond=0,
    tzinfo=ZoneInfo(TZ),
)

END_OF_DAY: Final[datetime] = datetime(
    year=YEAR,
    month=MONTH,
    day=DAY,
    hour=23,
    minute=59,
    second=59,
    microsecond=999999,
    tzinfo=ZoneInfo(TZ),
)

BEFORE_NOON: Final[datetime] = datetime(
    year=YEAR,
    month=MONTH,
    day=DAY,
    hour=11,
    minute=59,
    second=59,
    microsecond=999999,
    tzinfo=ZoneInfo(TZ),
)

AFTER_NOON: Final[datetime] = datetime(
    year=YEAR,
    month=MONTH,
    day=DAY,
    hour=12,
    minute=0,
    second=0,
    microsecond=1,
    tzinfo=ZoneInfo(TZ),
)


@pytest.mark.parametrize(
    "dt",
    [
        START_OF_DAY,
        NOON,
        END_OF_DAY,
        BEFORE_NOON,
        AFTER_NOON,
    ],
)
def test_get_noon_on_same_day(dt: datetime) -> None:
    assert get_noon_on_same_day(dt, TZ) == NOON
