from datetime import datetime

from adamant_armadillo_domain import DayOfWeek


def test_from_datetime() -> None:
    assert DayOfWeek.from_datetime(datetime(2026, 5, 2)) == DayOfWeek.SATURDAY
