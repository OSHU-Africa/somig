"""Valide les cas de pannes SOMIG.

Usage : python validate.py
Prérequis : pip install jsonschema
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

BASE = Path(__file__).parent
schema = json.loads((BASE / "schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(schema)

errors = 0
ids = set()

for path in sorted((BASE / "cases").glob("*.json")):
    case = json.loads(path.read_text(encoding="utf-8"))
    problems = [f"{'/'.join(map(str, e.path)) or 'racine'} : {e.message}" for e in validator.iter_errors(case)]

    if not problems:
        steps = {s["id"] for s in case["diagnostic"]}
        causes = {c["id"] for c in case["causes"]}
        if "E1" not in steps:
            problems.append("l'étape E1 est absente")
        targets = {r["vers"] for s in case["diagnostic"] for r in s["reponses"]}
        for t in sorted(targets - steps - causes):
            problems.append(f"destination inconnue : {t}")
        for c in sorted(causes - targets):
            problems.append(f"cause jamais atteinte : {c}")
        if case["id"] in ids:
            problems.append(f"identifiant en double : {case['id']}")
        ids.add(case["id"])

    status = "OK" if not problems else "ERREUR"
    print(f"[{status}] {path.name}")
    for p in problems:
        print(f"    - {p}")
    errors += len(problems)

sys.exit(1 if errors else 0)
