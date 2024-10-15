from django.urls import path
from .views import TeamView, PlayerDetailView, MatchView, AreaView

# URL patterns for the sports app
urlpatterns = [
    # URL pattern for retrieving a list of all teams
    path('teams/', TeamView.as_view(), name='teams'),

    # URL pattern for retrieving a list of all players
    path('players/', PlayerDetailView.as_view(), name='players'),

    # URL pattern for retrieving a list of all matches
    path('matches/', MatchView.as_view(), name='matches'),

    # URL pattern for retrieving a list of all areas
    path('areas/', AreaView.as_view(), name='areas'),
]
