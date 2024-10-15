from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Team, PlayerDetail, Match, Area
from django.forms.models import model_to_dict
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TeamView(APIView):
    """
    API View to retrieve a list of all teams.
    """

    @swagger_auto_schema(
        operation_description="Retrieve a list of all teams",
        responses={200: openapi.Response(
            'List of teams',
            examples={
                'application/json': [
                    {"id": 1, "name": "Team A", "coach": "Coach A"},
                    {"id": 2, "name": "Team B", "coach": "Coach B"},
                ]
            }
        )}
    )
    def get(self, request):
        """
        GET method to retrieve all teams.
        """
        teams = Team.objects.all()
        teams_list = [model_to_dict(team) for team in teams]
        return JsonResponse(teams_list, safe=False)

class PlayerDetailView(APIView):
    """
    API View to retrieve a list of all players.
    """

    @swagger_auto_schema(
        operation_description="Retrieve a list of all players",
        responses={200: openapi.Response(
            'List of players',
            examples={
                'application/json': [
                    {"id": 1, "name": "Player 1", "age": 25, "team": 1},
                    {"id": 2, "name": "Player 2", "age": 27, "team": 2},
                ]
            }
        )}
    )
    def get(self, request):
        """
        GET method to retrieve all players.
        """
        players = PlayerDetail.objects.all()
        players_list = [model_to_dict(player) for player in players]
        return JsonResponse(players_list, safe=False)

class MatchView(APIView):
    """
    API View to retrieve a list of all matches.
    """

    @swagger_auto_schema(
        operation_description="Retrieve a list of all matches",
        responses={200: openapi.Response(
            'List of matches',
            examples={
                'application/json': [
                    {"id": 1, "home_team": 1, "away_team": 2, "date": "2024-10-15T14:30:00Z", "location": 1},
                    {"id": 2, "home_team": 2, "away_team": 1, "date": "2024-10-16T14:30:00Z", "location": 2},
                ]
            }
        )}
    )
    def get(self, request):
        """
        GET method to retrieve all matches.
        """
        matches = Match.objects.all()
        matches_list = [model_to_dict(match) for match in matches]
        return JsonResponse(matches_list, safe=False)

class AreaView(APIView):
    """
    API View to retrieve a list of all areas.
    """

    @swagger_auto_schema(
        operation_description="Retrieve a list of all areas",
        responses={200: openapi.Response(
            'List of areas',
            examples={
                'application/json': [
                    {"id": 1, "name": "Stadium A", "city": "City A"},
                    {"id": 2, "name": "Stadium B", "city": "City B"},
                ]
            }
        )}
    )
    def get(self, request):
        """
        GET method to retrieve all areas.
        """
        areas = Area.objects.all()
        areas_list = [model_to_dict(area) for area in areas]
        return JsonResponse(areas_list, safe=False)

