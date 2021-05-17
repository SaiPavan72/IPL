from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PlayersForm
from .models import Players
import pdb


def teams_list(request):
    cursor = connection.cursor()
    cursor.execute('''select * from team_team''')
    teams = cursor.fetchall()
    return render(request, 'team/teamslist.html/', {'teams': teams})


def add_player(request):
    cursor = connection.cursor()
    cursor.execute('''select * from team_team''')
    team = cursor.fetchall()
    form = PlayersForm()
    return render(request, 'team/addplayer.html', {'form': form, 'team': team})


def save_player(request):
    if request.method == 'POST':
        form_obj = PlayersForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()

            return render(request, 'team/addplayer.html', {'form': PlayersForm(), 'error': form_obj.errors})

    return HttpResponseRedirect('/team/')


def team_players(request, id):
    cursor = connection.cursor()
    cursor.execute(f''' select *
    from team_team
    join team_players
    on team_team.id = team_players.team_id
    where team_team.id = {id}''')
    list1 = cursor.fetchall()
    # pdb.set_trace()
    return render(request, 'team/playerlist.html', {'player': list1})


def player_info(reequest, id):
    player = Players.objects.get(id=id)
    return render(reequest, 'team/playerinfo.html', {'player': player})
