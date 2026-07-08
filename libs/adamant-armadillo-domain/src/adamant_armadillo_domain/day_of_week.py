"""Utility class for representing the day of the week.

This module provides:
- DayOfWeek: a day of the week.
"""

from datetime import datetime
from enum import IntEnum


class DayOfWeek(IntEnum):
    """Enum class for representing the day of the week."""

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    @classmethod
    def from_datetime(cls: type[DayOfWeek], dt: datetime) -> DayOfWeek:
        """Calculate the day of the week for a datetime object.

        :param dt: datetime object. Source datetime to calculate the day of the week.
        :return: A DayOfWeek for the given datetime object.
        """
        return cls((dt.weekday() + 1) % 7)
