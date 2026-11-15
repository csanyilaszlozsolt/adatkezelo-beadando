import csv
import os

from data.basic.model import Team, Driver, Result


def write(teams: list[Team], drivers: list[Driver], results: list[Result], path: str, delimiter: str = ";") -> None:
    # minden tipus kulon fajlba, elso sor a mezonevek
    with open(os.path.join(path, "teams.csv"), "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "country", "founded"], delimiter=delimiter)
        writer.writeheader()
        for t in teams:
            writer.writerow(t.__dict__)

    with open(os.path.join(path, "drivers.csv"), "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "nationality", "number", "team_id"], delimiter=delimiter)
        writer.writeheader()
        for d in drivers:
            writer.writerow(d.__dict__)

    with open(os.path.join(path, "results.csv"), "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "grand_prix", "position", "points", "driver_id"], delimiter=delimiter)
        writer.writeheader()
        for r in results:
            writer.writerow(r.__dict__)


def read(path: str, delimiter: str = ";") -> tuple[list[Team], list[Driver], list[Result]]:
    # csv-ben minden szoveg, ezert a szamokat int()-tel vissza kell alakitani
    with open(os.path.join(path, "teams.csv"), "r", encoding="utf-8") as file:
        teams = [Team(row["id"], row["name"], row["country"], int(row["founded"]))
                 for row in csv.DictReader(file, delimiter=delimiter)]

    with open(os.path.join(path, "drivers.csv"), "r", encoding="utf-8") as file:
        drivers = [Driver(row["id"], row["name"], row["nationality"], int(row["number"]), row["team_id"])
                   for row in csv.DictReader(file, delimiter=delimiter)]

    with open(os.path.join(path, "results.csv"), "r", encoding="utf-8") as file:
        results = [Result(row["id"], row["grand_prix"], int(row["position"]), int(row["points"]), row["driver_id"])
                   for row in csv.DictReader(file, delimiter=delimiter)]

    return teams, drivers, results
