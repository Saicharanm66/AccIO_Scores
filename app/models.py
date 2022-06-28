from django.db import models
from django.contrib import admin

# Create your models here.

class TeamMember(models.Model):
    teamname=models.CharField(max_length=100)
    player_img= models.ImageField(upload_to='pics', blank=True)
    player_name=models.CharField(max_length=100)
    Type = (
        ("Fast Bowler", "Fast Bowler"),
    ("Spin Bowler", "Spin Bowler"),
    ("Medium Pace Bowler", "Medium Pace Bowler"),
    ("Batsmen", "Batsmen"),
    ("All Rounder", "All Rounder"),
    ("Wicket Keeper", "Wicket Keeper"),
    )
    Player_type = models.CharField(max_length=20,
                  choices=Type,
                  default="All Rounder")
    side=(
        ("Right hand", "Right hand"),
    ("Left hand", "Left hand"),)
    Player_side = models.CharField(max_length=20,
                  choices=side,
                  default="Right hand")
    
    def __str__(self):
           return str(self.teamname)+' : ' + str(self.player_name)
class Team(models.Model):
    #id= models.CharField(max_length=100)
    team_name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics', blank=True)
    desc= models.TextField(blank=True)
    Winnings= models.CharField(max_length=100,blank=True)
    team = models.ForeignKey(TeamMember, verbose_name=('Add Player'), on_delete=models.CASCADE, blank=True)
    def __str__(self):
           return 'Team: ' + self.team_name

class scoreupdate(models.Model):
    team1=models.CharField(max_length=1000)
    team2=models.CharField(max_length=1000)
    score= models.FloatField()
    wickets= models.IntegerField()
    over= models.FloatField()
    totalovers= models.FloatField(max_length=1000)
    currentbat1=models.CharField(max_length=1000, blank=True)
    currentbat1score=models.IntegerField()
    currentbat1balls=models.FloatField()
    currentbat2=models.CharField(max_length=1000, blank=True)
    currentbat2score=models.IntegerField()
    currentbat2balls=models.FloatField()
    currentbowler=models.CharField(max_length=1000, blank=True)
    commentry= models.CharField(max_length=100000, blank=True)
    def __str__(self):
           return 'Score'
class Schedule(models.Model):
    firstteam=models.CharField(max_length=100000)
    secondteam=models.CharField(max_length=100000)
    date=models.DateField(blank=True)
    time=models.TimeField(blank=True)
    Scheduled = (
        ("Ongoing", "ongoing"),
    ("Scheduled", "Scheduled"),
    ("Cancelled", "Cancelled"),
    )
    Status = models.CharField(max_length=20,
                  choices=Scheduled,
                  default="Scheduled")
    def __str__(self):
           return 'Match : *'+self.firstteam+'* vs *'+self.secondteam+' *'

    
#admin.site.register(Product, ProductAdmin)