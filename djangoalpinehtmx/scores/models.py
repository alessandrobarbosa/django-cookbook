from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')
    home_goals = models.IntegerField(blank=True, null=True)
    away_goals = models.IntegerField(blank=True, null=True)


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name="predictions")
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
