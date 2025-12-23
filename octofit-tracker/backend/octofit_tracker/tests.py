from django.test import TestCase

# Create your tests here for users, teams, activities, leaderboard, and workouts collections.
class BasicTestCase(TestCase):
    def test_basic(self):
        self.assertEqual(1, 1)
