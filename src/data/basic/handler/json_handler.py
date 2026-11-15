import json
import os

from data.basic.model import Team, Driver, Result


def write(teams: list[Team], drivers: list[Driver], results: list[Result], path: str, pretty: bool = True) -> None:
    # minden fajl egy lista, az elemei a rekordok (dict-ek)
    indent = 2 if pretty else None

    with open(os.path.join(path, "teams.json"), "w", encoding="utf-8") as file:
        json.dump([t.__dict__ for t in teams], file, indent=indent, ensure_ascii=False)

    with open(os.path.join(path, "drivers.json"), "w", encoding="utf-8") as file:
        json.dump([d.__dict__ for d in drivers], file, indent=indent, ensure_ascii=False)

    with open(os.path.join(path, "results.json"), "w", encoding="utf-8") as file:
        json.dump([r.__dict__ for r in results], file, indent=indent, ensure_ascii=False)


def read(path: str) -> tuple[list[Team], list[Driver], list[Result]]:
    # json megorzi a tipust (szam marad szam), ezert eleg a **doc kicsomagolas
    with open(os.path.join(path, "teams.json"), "r", encoding="utf-8") as file:
        teams = [Team(**doc) for doc in json.load(file)]

    with open(os.path.join(path, "drivers.json"), "r", encoding="utf-8") as file:
        drivers = [Driver(**doc) for doc in json.load(file)]

    with open(os.path.join(path, "results.json"), "r", encoding="utf-8") as file:
        results = [Result(**doc) for doc in json.load(file)]

    return teams, drivers, results
