import random
from faker import Faker

from data.basic.model import Team, Driver, Result

# F1 pontrendszer: 1. hely 25 pont ... 10. hely 1 pont, utana 0
POINTS = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]


def generate_teams(n: int, locale: str = "en_US", unique: bool = False,
                   min_year: int = 1950, max_year: int = 2020) -> list[Team]:
    assert n > 0
    assert 1900 <= min_year <= max_year <= 2026

    fake = Faker(locale)
    generator = fake.unique if unique else fake
    teams = []
    for i in range(n):
        teams.append(Team(
            "T-" + str(i + 1).zfill(3),
            generator.last_name() + " Racing",
            fake.country(),
            random.randint(min_year, max_year)))

    return teams


def generate_drivers(n: int, teams: list[Team], locale: str = "en_US", unique: bool = False,
                     female_ratio: float = 0.1) -> list[Driver]:
    assert n > 0
    assert len(teams) > 0
    assert n <= 99  # rajtszam 1-99 kozott, nem lehet ket egyforma
    assert 0 <= female_ratio <= 1

    fake = Faker(locale)
    generator = fake.unique if unique else fake
    numbers = random.sample(range(1, 100), n)
    drivers = []
    for i in range(n):
        # a fake.name() neha Dr.-t ad a nev ele
        female = random.random() < female_ratio
        first_name = generator.first_name_female() if female else generator.first_name_male()
        name = first_name + " " + fake.last_name()
        # igy minden csapatnak lesz pilotaja
        team = teams[i % len(teams)]
        drivers.append(Driver(
            "D-" + str(i + 1).zfill(3),
            name,
            fake.country(),
            numbers[i],
            team.id))

    return drivers


def generate_results(n: int, drivers: list[Driver], locale: str = "en_US",
                     field_size: int = 20, grand_prix: list[str] = None) -> list[Result]:
    assert n > 0
    assert len(drivers) > 0
    assert 1 <= field_size <= 30

    fake = Faker(locale)
    results = []
    for i in range(n):
        driver = random.choice(drivers)
        position = random.randint(1, field_size)
        points = POINTS[position - 1] if position <= 10 else 0
        gp = random.choice(grand_prix) if grand_prix else fake.city() + " Grand Prix"
        results.append(Result(
            "R-" + str(i + 1).zfill(4),
            gp,
            position,
            points,
            driver.id))

    return results


def generate_all(n: int):
    # n csapat, csapatonkent 2 pilota, pilotankent 5 eredmeny
    teams = generate_teams(n)
    drivers = generate_drivers(n * 2, teams)
    results = generate_results(n * 2 * 5, drivers)
    return teams, drivers, results
