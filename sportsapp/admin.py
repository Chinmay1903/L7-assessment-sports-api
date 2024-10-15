from django.contrib import admin
from .models import Team, Area, PlayerDetail, Match

# Register the Team model to make it accessible in the Django admin interface.
admin.site.register(Team)

# Register the Area model to make it accessible in the Django admin interface.
admin.site.register(Area)

# Register the PlayerDetail model to make it accessible in the Django admin interface.
admin.site.register(PlayerDetail)

# Register the Match model to make it accessible in the Django admin interface.
admin.site.register(Match)
