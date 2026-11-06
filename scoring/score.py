import json
import sys
from pathlib import Path

WEIGHTS = {"functional": 40, "algorithm": 25, "interaction": 15, "engineering": 20}
REQUIRED = {"status", "challenge_id", "challenge_version", "commit_sha", "score", "reasons", "metrics"}

def evaluate(result):
    missing = REQUIRED - result.keys()
    if missing:
        return {"status": "UNSCORED", "score": None, "reasons": [f"missing fields: {sorted(missing)}"]}
    if result["status"] != "PASS":
        return {"status": result["status"], "score": None, "reasons": result["reasons"]}
    if not result["commit_sha"] or not result["metrics"].get("wall_seconds") >= 0:
        return {"status": "UNSCORED", "score": None, "reasons": ["evidence is incomplete"]}
    dimensions = result.get("dimensions")
    if not isinstance(dimensions, dict) or any(k not in dimensions for k in WEIGHTS):
        return {"status": "UNSCORED", "score": None, "reasons": ["dimensions are not machine assessed"]}
    score = round(sum(float(dimensions[k]) for k in WEIGHTS), 2)
    if any(float(dimensions[k]) < 0 or float(dimensions[k]) > WEIGHTS[k] for k in WEIGHTS):
        return {"status": "UNSCORED", "score": None, "reasons": ["dimension is outside its declared maximum"]}
    return {"status": "PASS", "score": score, "reasons": [], "dimensions": dimensions}

if __name__ == "__main__":
    payload = json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps(evaluate(payload), ensure_ascii=False, sort_keys=True))
