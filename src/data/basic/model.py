from dataclasses import dataclass


@dataclass
class Team:
    id: str
    name: str
    country: str
    founded: int


@dataclass
class Driver:
    id: str
    name: str
    nationality: str
    number: int
    team_id: str  # melyik csapatban van


@dataclass
class Result:
    id: str
    grand_prix: str
    position: int
    points: int
    driver_id: str  # kie az eredmeny


if __name__ == "__main__":
    # teszt
    t = Team("T-001", "Teszt Racing", "Hungary", 1999)
    d = Driver("D-001", "Teszt Elek", "Hungary", 44, t.id)
    r = Result("R-001", "Hungaroring Grand Prix", 1, 25, d.id)
    print(t)
    print(d)
    print(r)
