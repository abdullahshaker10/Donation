from django.core.management.base import BaseCommand
from root.users.models import User
class Command(BaseCommand):
    help = 'Create a default superuser if not already exists'

    def handle(self, *args, **kwargs):
        email = "a@gmail.com"
        password = "a"
        user_name = "a"
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser {user_name} created successfully."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser {user_name} already exists."))