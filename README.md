# Curaçao Turtle Monitoring

Monitors sea turtle nesting activity, hatching success, and turtle encounters around the island of Curaçao. The workflow pulls nesting surveys, hatching inspections, nest relocations, and turtle encounter records from EarthRanger and produces a dashboard of maps, time series, and hatching success breakdowns by species, beach, and nest manipulation type.

## Dashboard widgets

| Widget | Description |
|--------|-------------|
| Total Nesting Events | Count of all nesting events in the selected period |
| Total Hatched Eggs | Sum of hatched/empty egg shells across all clutches |
| Hatching Success (%) | Hatched eggs ÷ total eggs × 100 |
| Total Turtle-Related Events | Count of all turtle encounter events |
| Total Turtles with FP | Unique turtles recorded with fibropapillomatosis |
| Nesting Activity Map | Map of nesting event locations |
| Nesting Activity Over Time | Monthly nesting counts by species |
| Total Nesting Activity by Beach | Breakdown of nesting types (Suspected Nest, Attempt, Dry Run) per beach |
| Nesting Success by Species & Beach | Hatching success metrics grouped by species and beach |
| Nesting Success by Nest Manipulation | Hatching success by manipulation type (Confirmed, Suspected, Relocated, Surprise Nest) |
| Turtle-Related Events Map | Map of all turtle encounter locations |
| Turtle Events by Location & Activity | Activity type breakdown (Netting, Rescue, Stranding, Nesting, Handcatch, Release) per location |
| FP Monitoring by Location | Fibropapillomatosis cases by location and activity type |

## Event types

| Event type | Used for |
|------------|----------|
| `suspected_nest_v2` | Nesting surveys — suspected nests |
| `attempt_v2` | Nesting surveys — false crawls / attempts |
| `dry_run_v2` | Nesting surveys — dry runs |
| `hatching_data` | Hatching inspections with egg counts |
| `relocation_data_v2` | Relocated nest records |
| `turtle_data_form_v2` | Turtle encounter records (captures, rescues, strandings) |