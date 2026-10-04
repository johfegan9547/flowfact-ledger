"""Verify the FlowFact hash chain. Usage: python verify.py [folder]   (Python 3, no packages needed)"""
import hashlib, json, sys
from pathlib import Path

base = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
sha = lambda s: hashlib.sha256(s if isinstance(s, bytes) else s.encode("utf-8")).hexdigest()
prev, bad, n, checked = "0" * 64, [], 0, 0
for line in (base / "chain.jsonl").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    c = json.loads(line); n += 1
    if c["prev"] != prev: bad.append(c["date"] + ": link broken")
    if sha(c["prev"] + c["date"] + c["file_sha256"]) != c["chain_sha256"]: bad.append(c["date"] + ": link hash wrong")
    f = base / "labels" / c["date"][:4] / (c["date"] + ".jsonl")
    if f.exists():
        checked += 1
        if sha(f.read_bytes()) != c["file_sha256"]: bad.append(c["date"] + ": file changed after it was chained")
    prev = c["chain_sha256"]
print(f"{n} days in the chain, {checked} released day files checked, head {prev}")
print("OK — nothing was changed" if not bad else "PROBLEMS:\n" + "\n".join(bad))
sys.exit(1 if bad else 0)
