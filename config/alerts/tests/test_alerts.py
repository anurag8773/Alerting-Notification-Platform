from django.test import TestCase
from django.contrib.auth.models import User
from alerts.models import Team, Profile, Alert, Notification

class AlertTestCase(TestCase):
    def setUp(self):
        team = Team.objects.create(name="QA")
        user = User.objects.create_user(username="john", password="pass123")
        Profile.objects.create(user=user, team=team)
        Alert.objects.create(title="Test Alert", message="Check system", team=team)

    def test_alert_created(self):
        self.assertEqual(Alert.objects.count(), 1)

    def test_profile_links_team(self):
        profile = Profile.objects.first()
        self.assertEqual(profile.team.name, "QA")

    def test_user_receives_notifications(self):
        user = User.objects.get(username="john")
        alert = Alert.objects.first()
        notif = Notification.objects.create(user=user, alert=alert)
        self.assertTrue(notif)
        self.assertEqual(notif.alert.title, "Test Alert")
