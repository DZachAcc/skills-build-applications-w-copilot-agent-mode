from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['spiderman', 'ironman', 'hulk'])
        dc = Team.objects.create(name='DC', members=['batman', 'superman', 'wonderwoman'])

        # Create users
        users = [
            User.objects.create(username='spiderman', email='spiderman@marvel.com'),
            User.objects.create(username='ironman', email='ironman@marvel.com'),
            User.objects.create(username='hulk', email='hulk@marvel.com'),
            User.objects.create(username='batman', email='batman@dc.com'),
            User.objects.create(username='superman', email='superman@dc.com'),
            User.objects.create(username='wonderwoman', email='wonderwoman@dc.com'),
        ]

        # Create activities
        Activity.objects.create(user='spiderman', type='run', duration=30, date='2025-12-01')
        Activity.objects.create(user='ironman', type='cycle', duration=45, date='2025-12-02')
        Activity.objects.create(user='hulk', type='swim', duration=60, date='2025-12-03')
        Activity.objects.create(user='batman', type='run', duration=25, date='2025-12-01')
        Activity.objects.create(user='superman', type='cycle', duration=50, date='2025-12-02')
        Activity.objects.create(user='wonderwoman', type='swim', duration=70, date='2025-12-03')

        # Create leaderboard
        Leaderboard.objects.create(user='spiderman', score=100)
        Leaderboard.objects.create(user='ironman', score=90)
        Leaderboard.objects.create(user='hulk', score=80)
        Leaderboard.objects.create(user='batman', score=95)
        Leaderboard.objects.create(user='superman', score=85)
        Leaderboard.objects.create(user='wonderwoman', score=75)

        # Create workouts
        Workout.objects.create(name='Morning Cardio', description='Run and cycle', difficulty='Easy')
        Workout.objects.create(name='Strength Training', description='Weights and resistance', difficulty='Medium')
        Workout.objects.create(name='Endurance Swim', description='Long distance swim', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
