"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path
from octofit_tracker import views

def get_api_url(request, endpoint):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev/api/'
    else:
        base_url = request.build_absolute_uri('/api/')
    return base_url + endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name='api-root'),
    path('api/users/', views.user_list, name='user-list'),
    path('api/teams/', views.team_list, name='team-list'),
    path('api/activities/', views.activity_list, name='activity-list'),
    path('api/leaderboard/', views.leaderboard_list, name='leaderboard-list'),
    path('api/workouts/', views.workout_list, name='workout-list'),
    path('', views.api_root, name='api-root-redirect'),
]
