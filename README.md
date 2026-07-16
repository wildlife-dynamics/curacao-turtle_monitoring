# Curaçao Turtle Monitoring

**[Full setup and configuration guide](https://wildlife-dynamics.github.io/curacao-turtle_monitoring/)** — A step-by-step walkthrough on how to set up and run the workflow.

This workflow monitors sea turtle nesting activity, hatching success, and turtle encounters around the island of Curaçao. It connects to EarthRanger to retrieve nesting surveys, hatching inspections, nest relocation records, and turtle encounter data. The workflow then produces a dashboard featuring maps, time series, and hatching success tables, broken down by species, beach, and nest manipulation type.

## Dashboard widgets

| Widget | Description |
|--------|-------------|
| Total Nesting Events | Count of all nesting events in the selected period |
| Total Hatched Eggs | Sum of hatched/empty egg shells across all inspected clutches |
| Hatching Success (%) | Hatched eggs ÷ total eggs × 100 |
| Total Turtle-Related Events | Count of all turtle encounter events |
| Total Turtles with FP | Unique turtles recorded with fibropapillomatosis |
| Nesting Activity Map | Interactive map of nesting event locations colored by type |
| Nesting Activity Over Time | Monthly nesting counts grouped by species |
| Total Nesting Activity by Beach | Breakdown of nesting types per beach |
| Nesting Success by Species & Beach | Hatching success metrics grouped by species and beach |
| Nesting Success by Nest Manipulation | Hatching success by manipulation type (Confirmed, Suspected, Relocated, Surprise Nest) |
| Turtle-Related Events Map | Interactive map of turtle encounter locations colored by activity type |
| Turtle Events by Location & Activity | Encounter counts broken down by location and activity type |
| FP Monitoring by Location | Fibropapillomatosis cases by location and activity type |

## Event types

| Event type | Used for |
|------------|----------|
| (suspected) Nest | Suspected nesting crawls |
| Attempt | False crawls / nesting attempts |
| Dry run | Dry runs (no eggs laid) |
| Hatching Data | Hatching inspections with egg counts |
| Relocation Data | Relocated nest records |
| Turtle Data Form | Turtle encounter records (netting, rescue, stranding, handcatch, release) |

## Requirements

[pixi](https://pixi.sh) is required for environment and dependency management. You will also need an EarthRanger connection configured in Ecoscope Desktop.
