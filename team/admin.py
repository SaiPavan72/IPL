from django.contrib import admin

from team.models import Team,Players,Matches,Points

admin.site.register(Team)
admin.site.register(Players)
admin.site.register(Matches)
admin.site.register(Points)
