import os

from django.core.management.base import BaseCommand

from root.users.enums import UserRoles
from root.users.models import Permission, Role, User


class Command(BaseCommand):
    help = "Create a default superuser if not already exists"

    def handle(self, *args, **kwargs):
        self.create_rules_and_permissions()
        self.create_super_user()
        self.create_investor_user()

    def create_super_user(self):
        email = os.getenv("ADMIN_EMAIL", "admin@gmail.com")
        password = os.getenv("ADMIN_PASSWORD")
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_superuser(email=email, password=password)
            user.role = Role.objects.get(name=UserRoles.ADMIN.value[0])
            user.save()

    def create_investor_user(self):
        email = os.getenv("INVESTOR_EMAIL", "investor@gmail.com")
        password = os.getenv("INVESTOR_PASSWORD")
        if not password:
            raise ValueError("INVESTOR_PASSWORD environment variable is required")
        user, _ = User.objects.get_or_create(email=email, password=password)
        user.role = Role.objects.get(name=UserRoles.INVESTOR.value[0])
        user.save()

    def create_rules_and_permissions(self):
        print("start creating rules")
        investor_role, _ = Role.objects.get_or_create(name=UserRoles.INVESTOR.value[0])
        for permission in UserRoles.permissions_for(UserRoles.INVESTOR.name):
            Permission.objects.get_or_create(name=permission[0], role=investor_role)
        print("finish creating rules")
