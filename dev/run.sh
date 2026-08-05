#!/bin/bash
set -e

# Usage:
#   bash dev/run.sh              # icons off (default)
#   bash dev/run.sh --icons-on   # icons on

PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
WORKFLOW_DIR="$PROJECT_DIR/ecoscope-workflows-turtle-monitoring-workflow"
RESULTS_DIR="/tmp/curacao-run-results"

ICONS_ON=false
for arg in "$@"; do
  case $arg in
    --icons-on) ICONS_ON=true ;;
    *) echo "Unknown option: $arg"; exit 1 ;;
  esac
done

# Build config file
if [ "$ICONS_ON" = true ]; then
  CONFIG_FILE="/tmp/curacao-run-params.yaml"
  cat > "$CONFIG_FILE" << 'YAML'
workflow_details:
  name: "Curacao Turtle Monitoring"
  description: ""
er_client:
  data_source:
    name: curacao
time_range:
  since: "2025-01-01T00:00:00.000Z"
  until: "2026-07-01T00:00:00.000Z"
nesting_layer:
  use_icons: true
YAML
  echo "Mode: icons ON"
else
  CONFIG_FILE="$PROJECT_DIR/param.yaml"
  echo "Mode: icons OFF (default)"
fi

rm -rf "$RESULTS_DIR" && mkdir -p "$RESULTS_DIR"
echo "Results: $RESULTS_DIR"
echo ""

cd "$WORKFLOW_DIR"
ECOSCOPE_WORKFLOWS_RESULTS="file://${RESULTS_DIR}" \
  pixi run --locked -e default \
  python -m ecoscope_workflows_turtle_monitoring_workflow.cli run \
    --config-file "$CONFIG_FILE" \
    --execution-mode sequential

# Check result
ERROR=$(python3 -c "import json; r=json.load(open('$RESULTS_DIR/result.json')); print(r.get('error') or '')" 2>/dev/null)
if [ -n "$ERROR" ]; then
  echo ""
  echo "✗ FAILED: $ERROR"
  exit 1
fi

echo ""
echo "✓ Workflow completed. Outputs:"
ls "$RESULTS_DIR"/*.html 2>/dev/null | while read f; do echo "  $f"; done
echo ""
echo "Open maps:"
echo "  open $RESULTS_DIR/*_nesting_map.html"
echo "  open $RESULTS_DIR/*_turtle_map.html"
