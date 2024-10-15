from django.test import TestCase
from .models import Team, Area, PlayerDetail, Match
from django.utils import timezone
from datetime import timedelta

class TeamModelTest(TestCase):
    """
    Test case for the Team model.
    """

    def setUp(self):
        """
        Set up a test team instance.
        """
        self.team = Team.objects.create(name='Red Warriors', coach='John Doe')

    def test_team_creation(self):
        """
        Test the creation of a team instance.
        """
        self.assertEqual(self.team.name, 'Red Warriors')
        self.assertEqual(self.team.coach, 'John Doe')
        self.assertIsNotNone(self.team.created_at)  # Check if created_at is set

    def test_string_representation(self):
        """
        Test the string representation of a team instance.
        """
        self.assertEqual(str(self.team), 'Red Warriors')

class AreaModelTest(TestCase):
    """
    Test case for the Area model.
    """

    def setUp(self):
        """
        Set up a test area instance.
        """
        self.area = Area.objects.create(name='Downtown', city='Metropolis')

    def test_area_creation(self):
        """
        Test the creation of an area instance.
        """
        self.assertEqual(self.area.name, 'Downtown')
        self.assertEqual(self.area.city, 'Metropolis')
        self.assertIsNotNone(self.area.created_at)  # Check if created_at is set

    def test_string_representation(self):
        """
        Test the string representation of an area instance.
        """
        self.assertEqual(str(self.area), 'Downtown')

class PlayerDetailModelTest(TestCase):
    """
    Test case for the PlayerDetail model.
    """

    def setUp(self):
        """
        Set up a test player instance.
        """
        self.team = Team.objects.create(name='Blue Knights', coach='Jane Doe')
        self.player = PlayerDetail.objects.create(name='Alice', age=25, team=self.team)

    def test_player_creation(self):
        """
        Test the creation of a player instance.
        """
        self.assertEqual(self.player.name, 'Alice')
        self.assertEqual(self.player.age, 25)
        self.assertEqual(self.player.team, self.team)
        self.assertIsNotNone(self.player.created_at)  # Check if created_at is set

    def test_string_representation(self):
        """
        Test the string representation of a player instance.
        """
        self.assertEqual(str(self.player), 'Alice(25) in Blue Knights')

class MatchModelTest(TestCase):
    """
    Test case for the Match model.
    """

    def setUp(self):
        """
        Set up a test match instance.
        """
        self.team1 = Team.objects.create(name='Team A', coach='Coach A')
        self.team2 = Team.objects.create(name='Team B', coach='Coach B')
        self.area = Area.objects.create(name='Stadium', city='Metropolis')
        self.match = Match.objects.create(
            home_team=self.team1,
            away_team=self.team2,
            date=timezone.now() + timedelta(days=1),  # Match is scheduled for tomorrow
            location=self.area
        )

    def test_match_creation(self):
        """
        Test the creation of a match instance.
        """
        self.assertEqual(self.match.home_team, self.team1)
        self.assertEqual(self.match.away_team, self.team2)
        self.assertEqual(self.match.location, self.area)
        self.assertIsNotNone(self.match.created_at)  # Check if created_at is set
        self.assertIsInstance(self.match.date, timezone.datetime)  # Check if date is a datetime object

    def test_string_representation(self):
        """
        Test the string representation of a match instance.
        """
        self.assertEqual(str(self.match), 'Team A vs Team B')
