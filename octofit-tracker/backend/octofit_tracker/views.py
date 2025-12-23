from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })

# Example list views (to be expanded)
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def team_list(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def activity_list(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def leaderboard_list(request):
    leaderboard = Leaderboard.objects.all()
    serializer = LeaderboardSerializer(leaderboard, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def workout_list(request):
    workouts = Workout.objects.all()
    serializer = WorkoutSerializer(workouts, many=True)
    return Response(serializer.data)
