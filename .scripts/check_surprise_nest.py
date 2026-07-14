"""
Test regex-based manipulation type derivation against all hatching_data records up to today.
Format: YYMMDD-XX-[SCR]N-N  →  capture group 1 = manipulation char.
Surprise Nest = free-text containing 'surprise'.
"""
import os
import re
from collections import Counter
from ecoscope.io import EarthRangerIO

_MANIPULATION_MAP = {
    "S": "Suspected Nest",
    "C": "Confirmed Nest",
    "R": "Relocated",
}
_ID_PATTERN = re.compile(r"^\d{6}-\w{2}-([SCR])", re.IGNORECASE)


def _derive_manipulation_type(activity_id: str) -> str:
    if not isinstance(activity_id, str) or not activity_id.strip():
        return "Unknown"
    if "surprise" in activity_id.lower():
        return "Surprise Nest"
    m = _ID_PATTERN.match(activity_id)
    if m:
        return _MANIPULATION_MAP.get(m.group(1).upper(), "Unknown")
    return "Unknown"


prefix = "ECOSCOPE_WORKFLOWS__CONNECTIONS__EARTHRANGER__curacao__"
er = EarthRangerIO(
    server=os.environ[prefix + "SERVER"],
    username=os.environ[prefix + "USERNAME"],
    password=os.environ[prefix + "PASSWORD"],
    tcp_limit=5,
    sub_page_size=4000,
)

print("Fetching all events up to today...")
df = er.get_events(
    since="2025-01-01T00:00:00.000Z",
    until="2026-07-14T23:59:59.000Z",
    include_details=True,
)
df = df[df["event_type"] == "hatching_data"].reset_index(drop=True)

if df.empty:
    print("No hatching_data events found.")
else:
    print(f"Total hatching_data records: {len(df)}\n")

    ids = df["event_details"].str.get("original_activity_id").fillna("").astype(str)
    derived = ids.map(_derive_manipulation_type)

    print("--- Derived manipulation type counts ---")
    for label, count in Counter(derived).most_common():
        print(f"  {label:<20} → {count}")

    print(f"\n--- All records (original_activity_id → derived type) ---")
    for raw, label in sorted(zip(ids, derived)):
        print(f"  {label:<20}  {raw!r}")
