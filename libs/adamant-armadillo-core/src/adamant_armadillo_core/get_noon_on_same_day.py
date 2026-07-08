"""Utility function for calculating a datetime representing noon on the same day.

This module provides:
- get_noon_on_same_day: calculate noon on the same day.
"""

from datetime import datetime
from zoneinfo import ZoneInfo


def get_noon_on_same_day(dt: datetime, timezone: str) -> datetime:
    """Calculate noon on the same day for the given datetime and timezone.

    :param dt: Source datetime whose year, month, and day are used.
    :param timezone: IANA timezone name, such as "America/New_York".
    :return: A timezone-aware datetime representing noon.
    :rtype: datetime
    """
    return datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=12,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=ZoneInfo(timezone),
    )
