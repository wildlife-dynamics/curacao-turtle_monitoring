"""
Inspect actual event data from Curacao ER to understand old vs v2 field structures.
"""
import json
import os
from ecoscope.io import EarthRangerIO

prefix = "ECOSCOPE_WORKFLOWS__CONNECTIONS__EARTHRANGER__curacao__"
er = EarthRangerIO(
    server=os.environ[prefix + "SERVER"],
    username=os.environ[prefix + "USERNAME"],
    password=os.environ[prefix + "PASSWORD"],
    tcp_limit=5,
    sub_page_size=4000,
)

OLD_TO_NEW = {
    "nestingdata": "suspected_nest_v2",
    "attemptevent": "attempt_v2",
    "dryrunevent": "dry_run_v2",
    "hatchdata": "hatching_data",
    "relocdata": "relocation_data_v2",
    "turtledataform": "turtle_data_form_v2",
}

print("Fetching all events...")
all_events = er.get_events(
    since="2022-01-01T00:00:00.000Z",
    until="2026-01-01T00:00:00.000Z",
    include_details=True,
)

print(f"\nTotal events: {len(all_events)}")
print("\nEvent type counts:")
print(all_events["event_type"].value_counts().to_string())

print("\n" + "=" * 60)
for old_type, new_type in OLD_TO_NEW.items():
    subset = all_events[all_events["event_type"] == old_type]
    if len(subset) == 0:
        continue
    sample = subset.iloc[0]
    details = sample.get("event_details", {}) or {}
    print(f"\n{old_type} (→ {new_type}) — {len(subset)} events")
    print(f"  Fields in event_details: {list(details.keys())}")
    # Show sample values for first 3 fields
    for k, v in list(details.items())[:5]:
        print(f"    {k}: {repr(v)[:60]}")
