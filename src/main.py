import os

from data.basic.generator import generate_all, generate_teams, generate_drivers, generate_results
from data.basic.handler import csv_handler, json_handler, xlsx_handler

OUTPUT = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT, exist_ok=True)

teams, drivers, results = generate_all(5)
print("Generalva:", len(teams), "csapat,", len(drivers), "pilota,", len(results), "eredmeny")

# CSV
csv_handler.write(teams, drivers, results, OUTPUT)
t2, d2, r2 = csv_handler.read(OUTPUT)
print("CSV visszaolvasva, egyezik:", t2 == teams and d2 == drivers and r2 == results)

# JSON
json_handler.write(teams, drivers, results, OUTPUT)
t2, d2, r2 = json_handler.read(OUTPUT)
print("JSON visszaolvasva, egyezik:", t2 == teams and d2 == drivers and r2 == results)

# XLSX
xlsx_handler.write(teams, drivers, results, OUTPUT)
t2, d2, r2 = xlsx_handler.read(OUTPUT)
print("XLSX visszaolvasva, egyezik:", t2 == teams and d2 == drivers and r2 == results)

# parameterezett generalas
print()
t = generate_teams(2, locale="hu_HU", min_year=2000, max_year=2010)
d = generate_drivers(4, t, locale="hu_HU", female_ratio=0.5)
r = generate_results(3, d, field_size=10, grand_prix=["Hungaroring", "Monaco", "Monza"])
for x in t + d + r:
    print(x)
