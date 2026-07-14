"""
Fetch raw event-type schemas from EarthRanger (Curacao) and write each to event-type/<name>.json.

Run with:
  cd /Users/zak/Documents/w-dynamics/Curacao-Turtle_Monitoring
  pixi run -e compile python .scripts/fetch_event_type_schemas.py
"""

import json
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

from tqdm import tqdm
from ecoscope_workflows_ext_ecoscope.connections import EarthRangerConnection

er = EarthRangerConnection.from_named_connection("curacao").get_client()
print(f"Connected: {er.server}\n")

EVENT_TYPES = [
    "suspected_nest_v2",
    "attempt_v2",
    "dry_run_v2",
    "hatching_data",
    "relocation_data_v2",
    "turtle_data_form_v2",
]

OUTPUT_DIR = Path(__file__).parent.parent / "event-type"
OUTPUT_DIR.mkdir(exist_ok=True)

for event_type in tqdm(EVENT_TYPES, desc="Fetching schemas"):
    try:
        with er._use_v2_api():
            schema = er._get(f"activity/eventtypes/{event_type}/schema")
        out_path = OUTPUT_DIR / f"{event_type}.json"
        out_path.write_text(json.dumps(schema, indent=2, ensure_ascii=False))
    except Exception as e:
        tqdm.write(f"ERROR {event_type}: {e}")

print(f"\nDone. Files written to: {OUTPUT_DIR}")
