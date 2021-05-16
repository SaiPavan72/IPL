from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PlayersForm
from .models import Players


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


def team_players(request,id):
    import pdb
    list = Players.objects.filter(team__id=id)
    return render(request, 'team/playerlist.html', {'list': list})