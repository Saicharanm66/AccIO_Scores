from django.shortcuts import render
from .models import Team, TeamMember, scoreupdate, Schedule
import os
# Create your views here.


def index(request):

    dests=Team.objects.all()
    score=scoreupdate.objects.all()

    return render(request, "index.html", {'dests': dests, 'score':score})
def about(request):
    score=scoreupdate.objects.all()
    return render(request, "about.html", {'score':score})
def schedules(request):
    sch=Schedule.objects.all()
    return render(request, "Schedule.html", {'sch': sch})
def teamss(request):
    tms=Team.objects.all()
    memb=TeamMember.objects.all()
    return render(request, "teams.html", {'tms': tms, 'memb':memb})
def teammember(request):
    memb=TeamMember.objects.all()
    return render(request, "tmat.html", {'memb':memb})
def teamsmembers(request):
    tms=Team.objects.all()
    memb=TeamMember.objects.all()
    return render(request, "teams.html", {'tms': tms, 'memb':memb})
    
    
