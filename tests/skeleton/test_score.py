import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sample = ROOT / "tests/skeleton/result.sample.json"
output = subprocess.check_output([sys.executable, str(ROOT / "scoring/score.py"), str(sample)], text=True)
result = json.loads(output)
assert result["status"] == "PASS"
assert result["score"] == 100
