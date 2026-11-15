import os

from data.basic.generator import generate_all
from data.basic.handler import csv_handler, json_handler, xlsx_handler

# a generalt fajlok a projekt output mappajaba kerulnek
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT, exist_ok=True)

# 1. adatok generalasa
teams, drivers, results = generate_all(5)
print("Generalva:", len(teams), "csapat,", len(drivers), "pilota,", len(results), "eredmeny")

# 2. kiiras es visszaolvasas mindharom formatumban
for name, handler in [("CSV", csv_handler), ("JSON", json_handler), ("XLSX", xlsx_handler)]:
    handler.write(teams, drivers, results, OUTPUT)
    t2, d2, r2 = handler.read(OUTPUT)
    ok = (t2 == teams and d2 == drivers and r2 == results)
    print(name, "- kiirva es visszaolvasva, egyezik:", ok)

print("\nPelda pilota:", drivers[0])
print("Fajlok helye:", os.path.abspath(OUTPUT))
