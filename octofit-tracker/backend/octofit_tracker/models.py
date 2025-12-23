from djongo import models

# User model (proxy for MongoDB collection)
class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=150)
    email = models.EmailField()
    # Add more fields as needed
    class Meta:
        managed = False
        db_table = 'users'

# Team model
class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)
    class Meta:
        managed = False
        db_table = 'teams'

# Activity model
class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        managed = False
        db_table = 'activities'

# Leaderboard model
class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=150)
    score = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'leaderboard'

# Workout model
class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'workouts'
