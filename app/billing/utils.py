from __future__ import annotations

from datetime import datetime, timezone, timedelta


def utc_ts_days_ago(days: int) -> int:
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=max(1, days))
    return int(start.timestamp())
