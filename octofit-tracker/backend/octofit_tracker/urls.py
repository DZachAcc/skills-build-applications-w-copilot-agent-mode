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
from django.contrib import admin
from django.urls import path
from octofit_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root, name='api-root'),
    path('users/', views.user_list, name='user-list'),
    path('teams/', views.team_list, name='team-list'),
    path('activities/', views.activity_list, name='activity-list'),
    path('leaderboard/', views.leaderboard_list, name='leaderboard-list'),
    path('workouts/', views.workout_list, name='workout-list'),
]
