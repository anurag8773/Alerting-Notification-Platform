from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from alerts.models import Team, Profile, Alert

class Command(BaseCommand):
    help = "Seed database with sample teams, users, profiles, and alerts"

    def handle(self, *args, **options):
        # Clear old data
        Alert.objects.all().delete()
        Profile.objects.all().delete()
        Team.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        # Create Teams
        engineering = Team.objects.create(name="Engineering")
        marketing = Team.objects.create(name="Marketing")

        # Create Users with Profiles
        u1 = User.objects.create_user(username="alice", password="pass123")
        Profile.objects.create(user=u1, team=engineering)

        u2 = User.objects.create_user(username="bob", password="pass123")
        Profile.objects.create(user=u2, team=engineering)

        u3 = User.objects.create_user(username="carol", password="pass123")
        Profile.objects.create(user=u3, team=marketing)

        # Create Alerts
        Alert.objects.create(title="System Upgrade",
                             message="Engineering servers will reboot at 10 PM.",
                             team=engineering)

        Alert.objects.create(title="New Campaign",
                             message="Marketing campaign launch at 9 AM tomorrow.",
                             team=marketing)

        self.stdout.write(self.style.SUCCESS("Seed data created successfully"))
