"""
MODULE: datetime_notes
Purpose: datetime operations with consistent docstring structure:
topic, function syntax, usage (this is CODE), real life usecases, pros, cons.
"""

from datetime import datetime, date, time, timedelta, timezone


# ------------------------------------------------------
def demo_datetime_now():
    """
    TOPIC:
        current datetime

    FUNCTION SYNTAX:
        datetime.now(tz=None)

    USAGE:
        now = datetime.now()

    REAL LIFE USECASES:
        - Timestamping logs.
        - Tracking request creation time.
        - Auditing events.

    PROS:
        - Simple and commonly used.
    CONS:
        - Timezone-naive by default (dangerous in distributed systems).
    """
    return datetime.now()


# ------------------------------------------------------
def demo_datetime_utcnow():
    """
    TOPIC:
        UTC datetime

    FUNCTION SYNTAX:
        datetime.utcnow()

    USAGE:
        now = datetime.utcnow()

    REAL LIFE USECASES:
        - Store timestamps in UTC in databases.
        - Avoid timezone ambiguity.

    PROS:
        - Consistent global time.
    CONS:
        - Still naive (no tzinfo). Prefer timezone-aware UTC.
    """
    return datetime.utcnow()


# ------------------------------------------------------
def demo_timezone_aware():
    """
    TOPIC:
        timezone-aware datetime

    FUNCTION SYNTAX:
        datetime.now(timezone.utc)

    USAGE:
        now = datetime.now(timezone.utc)

    REAL LIFE USECASES:
        - Production-grade systems.
        - APIs serving users across regions.
        - Financial and audit systems.

    PROS:
        - Explicit timezone handling.
    CONS:
        - Slightly more verbose.
    """
    return datetime.now(timezone.utc)


# ------------------------------------------------------
def demo_date_today():
    """
    TOPIC:
        current date

    FUNCTION SYNTAX:
        date.today()

    USAGE:
        today = date.today()

    REAL LIFE USECASES:
        - Daily reports.
        - Date-based partitions.
        - Scheduling logic.

    PROS:
        - Clean and simple.
    CONS:
        - No time information.
    """
    return date.today()


# ------------------------------------------------------
def demo_time_object():
    """
    TOPIC:
        time object

    FUNCTION SYNTAX:
        time(hour, minute, second)

    USAGE:
        t = time(10, 30, 0)

    REAL LIFE USECASES:
        - Store business hours.
        - Compare daily cut-off times.

    PROS:
        - Lightweight.
    CONS:
        - No date or timezone context.
    """
    return time(10, 30, 0)


# ------------------------------------------------------
def demo_datetime_components():
    """
    TOPIC:
        datetime components

    FUNCTION SYNTAX:
        dt.year, dt.month, dt.day, dt.hour

    USAGE:
        dt = datetime.now()
        y = dt.year

    REAL LIFE USECASES:
        - Grouping analytics by date/time.
        - Formatting custom outputs.

    PROS:
        - Easy attribute access.
    CONS:
        - Manual formatting if overused.
    """
    dt = datetime.now()
    return dt.year, dt.month, dt.day, dt.hour


# ------------------------------------------------------
def demo_strftime():
    """
    TOPIC:
        datetime to string

    FUNCTION SYNTAX:
        datetime.strftime(format)

    USAGE:
        dt.strftime("%Y-%m-%d %H:%M:%S")

    REAL LIFE USECASES:
        - API responses.
        - Log formatting.
        - Human-readable timestamps.

    PROS:
        - Full control over format.
    CONS:
        - Format strings must be remembered.
    """
    dt = datetime(2025, 1, 1, 10, 30)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# ------------------------------------------------------
def demo_strptime():
    """
    TOPIC:
        string to datetime

    FUNCTION SYNTAX:
        datetime.strptime(date_string, format)

    USAGE:
        dt = datetime.strptime("2025-01-01", "%Y-%m-%d")

    REAL LIFE USECASES:
        - Parsing user input dates.
        - Reading CSV / logs.

    PROS:
        - Strict parsing.
    CONS:
        - Raises ValueError if format mismatches.
    """
    return datetime.strptime("2025-01-01", "%Y-%m-%d")


# ------------------------------------------------------
def demo_timedelta():
    """
    TOPIC:
        timedelta (date arithmetic)

    FUNCTION SYNTAX:
        timedelta(days=0, hours=0, minutes=0)

    USAGE:
        dt + timedelta(days=1)

    REAL LIFE USECASES:
        - Expiry times (JWT, OTP).
        - Retry scheduling.
        - SLA calculations.

    PROS:
        - Very intuitive time math.
    CONS:
        - Months/years not supported directly.
    """
    now = datetime.now()
    return now, now + timedelta(days=1)


# ------------------------------------------------------
def demo_datetime_comparison():
    """
    TOPIC:
        datetime comparison

    FUNCTION SYNTAX:
        dt1 < dt2

    USAGE:
        expiry < now

    REAL LIFE USECASES:
        - Token expiry validation.
        - Session timeout logic.

    PROS:
        - Native comparison support.
    CONS:
        - Naive vs aware comparison raises error.
    """
    a = datetime(2025, 1, 1)
    b = datetime(2025, 1, 2)
    return a < b


# ------------------------------------------------------
def demo_timestamp():
    """
    TOPIC:
        unix timestamp

    FUNCTION SYNTAX:
        datetime.timestamp()

    USAGE:
        ts = datetime.now().timestamp()

    REAL LIFE USECASES:
        - Store compact time values.
        - Interop with JS / frontend.
        - Message ordering.

    PROS:
        - Universal numeric representation.
    CONS:
        - Less human-readable.
    """
    return datetime.now().timestamp()


# ------------------------------------------------------
def demo_fromtimestamp():
    """
    TOPIC:
        datetime from unix timestamp

    FUNCTION SYNTAX:
        datetime.fromtimestamp(ts, tz=None)

    USAGE:
        datetime.fromtimestamp(1700000000)

    REAL LIFE USECASES:
        - Convert stored timestamps.
        - Display frontend times.

    PROS:
        - Simple conversion.
    CONS:
        - Timezone must be handled carefully.
    """
    return datetime.fromtimestamp(1700000000)


# ------------------------------------------------------
def demo_isoformat():
    """
    TOPIC:
        ISO 8601 format

    FUNCTION SYNTAX:
        datetime.isoformat()

    USAGE:
        dt.isoformat()

    REAL LIFE USECASES:
        - REST APIs.
        - JSON serialization.
        - Cross-language compatibility.

    PROS:
        - Standardized format.
    CONS:
        - Slightly verbose for humans.
    """
    return datetime.now(timezone.utc).isoformat()


# ------------------------------------------------------
def demo_replace():
    """
    TOPIC:
        datetime.replace()

    FUNCTION SYNTAX:
        datetime.replace(**kwargs)

    USAGE:
        dt.replace(hour=0, minute=0)

    REAL LIFE USECASES:
        - Normalize timestamps.
        - Start-of-day calculations.

    PROS:
        - Non-mutating (returns new object).
    CONS:
        - Easy to misuse if not careful.
    """
    dt = datetime.now()
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)
