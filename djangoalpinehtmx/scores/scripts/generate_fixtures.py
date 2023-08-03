from scores.models import Team, Fixture


def run() -> None:
    """
    Execute this script using python manage.py runscript generate_fixtures.
    :return:
    """
    teams = [
        "Arsenal",
        "Chelsea",
        "Liverpool",
        "Manchester City",
        "Manchester United",
        "Tottenham Hotspur",
        "Real Madrid",
        "Barcelona",
        "Juventus",
        "Inter Milan",
        "Bayern Munich",
        "Ajax",
        "PSG",
        "Porto"
    ]

    for team in teams:
        Team.objects.get_or_create(name=team)

    teams = Team.objects.all()

    for team1, team2 in zip(teams[::2], teams[1::2]):
        print(f"Creating matches {team1} vs {team2}")
        Fixture.objects.get_or_create(home_team=team1, away_team=team2)
