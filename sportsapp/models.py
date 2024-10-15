from django.db import models

class Team(models.Model):
    """
    Model representing a sports team.
    """
    name = models.CharField(max_length=100, help_text="Name of the team")
    coach = models.CharField(max_length=100, help_text="Name of the coach")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the team was created")

    def __str__(self):
        """
        String representation of the Team model.
        """
        return self.name


class Area(models.Model):
    """
    Model representing an area or location.
    """
    name = models.CharField(max_length=100, help_text="Name of the area")
    city = models.CharField(max_length=100, help_text="City where the area is located")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the area was created")

    def __str__(self):
        """
        String representation of the Area model.
        """
        return self.name


class PlayerDetail(models.Model):
    """
    Model representing a player's details.
    """
    name = models.CharField(max_length=100, help_text="Name of the player")
    age = models.IntegerField(help_text="Age of the player")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, help_text="Team to which the player belongs")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the player was added")

    def __str__(self):
        """
        String representation of the PlayerDetail model.
        """
        return f'{self.name}({self.age}) in {self.team}'


class Match(models.Model):
    """
    Model representing a match between two teams.
    """
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE, help_text="Home team of the match")
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE, help_text="Away team of the match")
    date = models.DateTimeField(help_text="Date and time of the match")
    location = models.ForeignKey(Area, on_delete=models.CASCADE, help_text="Location where the match is held")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time when the match was created")

    def __str__(self):
        """
        String representation of the Match model.
        """
        return f'{self.home_team} vs {self.away_team}'
