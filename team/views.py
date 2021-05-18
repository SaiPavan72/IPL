from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PlayersForm
from .models import Players, Team, Matches, Points
import random
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

def matches(request):
    teams = Team.objects.all()
    team1 = random.choice(teams)
    ex = teams.exclude(team_name=team1.team_name)
    team2 = random.choice(ex)
    winner = random.choice((team1, team2))
    win_tm, flag = Points.objects.get_or_create(team=winner)
    win_tm.played += 1
    win_tm.won += 1
    win_tm.points += 2
    win_tm.save()
    if team1.team_name == win_tm.team.team_name:
        l_team = team2
    else:
        l_team = team1
    loss_tm, flag = Points.objects.get_or_create(team=l_team)
    loss_tm.played += 1
    loss_tm.lost += 1
    loss_tm.points += 0
    loss_tm.save()
    return render(request, "team/points_table.html", {"win": win_tm, "loss": loss_tm,"teams": teams})

def points(request):
    point=Points.objects.all
    return render(request,'team/points.html',{'point':point})
