import json, csv, os

base = os.path.dirname(__file__)
with open(os.path.join(base, "bikes.json")) as f:
    data = json.load(f)

def cell(v):
    if isinstance(v, dict):
        return f"{v.get('base','')} / {v.get('top','')}"
    return "" if v is None else str(v)

rows = []
for cat in data["categories"]:
    for r in cat["rows"]:
        rows.append([
            cat["name"], cat["priority"], r["label"],
            cell(r.get("mach2")), cell(r.get("superstreet")), cell(r.get("x47")),
        ])

out = os.path.join(base, "bikes_comparison.csv")
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Category", "Priority", "Spec", "F77 MACH 2 (base / top)", "F77 SUPERSTREET (base / top)", "X-47 (base / top)"])
    w.writerows(rows)

print(f"OK: {len(rows)} spec rows across {len(data['categories'])} categories -> {out}")
