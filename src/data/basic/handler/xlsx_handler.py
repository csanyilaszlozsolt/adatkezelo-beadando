import os
from openpyxl import Workbook, load_workbook

from data.basic.model import Team, Driver, Result


def write(teams: list[Team], drivers: list[Driver], results: list[Result], path: str,
          file_name: str = "f1.xlsx") -> None:
    # tipusonkent kulon munkalap
    wb = Workbook()

    ws = wb.active
    ws.title = "teams"
    ws.append(["id", "name", "country", "founded"])
    for t in teams:
        ws.append([t.id, t.name, t.country, t.founded])

    ws = wb.create_sheet("drivers")
    ws.append(["id", "name", "nationality", "number", "team_id"])
    for d in drivers:
        ws.append([d.id, d.name, d.nationality, d.number, d.team_id])

    ws = wb.create_sheet("results")
    ws.append(["id", "grand_prix", "position", "points", "driver_id"])
    for r in results:
        ws.append([r.id, r.grand_prix, r.position, r.points, r.driver_id])

    wb.save(os.path.join(path, file_name))


def read(path: str, file_name: str = "f1.xlsx"):
    wb = load_workbook(os.path.join(path, file_name))

    # elso sor a fejlec
    teams = [Team(*row) for row in wb["teams"].iter_rows(min_row=2, values_only=True)]
    drivers = [Driver(*row) for row in wb["drivers"].iter_rows(min_row=2, values_only=True)]
    results = [Result(*row) for row in wb["results"].iter_rows(min_row=2, values_only=True)]

    return teams, drivers, results
