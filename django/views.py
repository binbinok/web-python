from django.http import HttpResponse
from .models import Team

def index(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    return HttpResponse('Hello from Django!')