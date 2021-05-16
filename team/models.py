from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField(upload_to='media/')
    club_state = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Players(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_fname = models.CharField(max_length=100)
    player_lname = models.CharField(max_length=100)
    player_image = models.ImageField(upload_to='media1/')
    jersey_number = models.IntegerField(null=False,blank=False)
    player_country = models.CharField(max_length=100)
    total_matches=models.IntegerField(default=0)
    total_runs=models.IntegerField(default=0)
    hundreds=models.IntegerField(default=0)
    half_centuries=models.IntegerField(default=0)
    highest_score=models.IntegerField(default=0)
    total_wickets = models.IntegerField(default=0)
    highest_wickets = models.IntegerField(default=0)

    def __str__(self):
        return self.player_fname



class Match(models.Model):
    date = models.DateField()
    time = models.TimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    result = models.CharField(max_length=50, null=True, blank=True)


