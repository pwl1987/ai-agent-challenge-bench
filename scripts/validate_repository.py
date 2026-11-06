import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / "schema/challenge.schema.json").read_text())
required = set(schema["required"])
errors = []
for path in sorted((ROOT / "challenges").glob("*/challenge.json")):
    data = json.loads(path.read_text())
    missing = required - data.keys()
    if missing:
        errors.append(f"{path}: missing {sorted(missing)}")
    if data.get("scoring") != {"functional": 40, "algorithm": 25, "interaction": 15, "engineering": 20}:
        errors.append(f"{path}: scoring weights must be V0.1 constants")
    if not (path.parent / "AGENT_INSTRUCTION.md").exists():
        errors.append(f"{path}: missing AGENT_INSTRUCTION.md")
if not (ROOT / ".github/workflows/validate.yml").exists():
    errors.append("missing CI workflow")
if errors:
    raise SystemExit("\n".join(errors))
print(f"validated {len(list((ROOT / 'challenges').glob('*/challenge.json')))} challenges")
