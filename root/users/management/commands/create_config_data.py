from django.core.management.base import BaseCommand
from root.users.enums import UserRoles
from root.users.models import Permission, Role, User
class Command(BaseCommand):
    help = 'Create a default superuser if not already exists'

    def handle(self, *args, **kwargs):
        self.create_rules_and_permissions()
        self.create_super_user()
        self.create_investor_user()

    def create_super_user(self):
        email = "a@gmail.com"
        password = "a"
        if not User.objects.filter(email=email).exists():
            user = User.objects.create_superuser(email=email, password=password)
            user.role = Role.objects.get(name=UserRoles.ADMIN.value[0])
            user.save()
    def create_investor_user(self):
        email = "investor@gmail.com"
        password = "a"
        user,_ = User.objects.get_or_create(email=email, password=password)
        user.role = Role.objects.get(name=UserRoles.INVESTOR.value[0])
        user.save()

    def create_rules_and_permissions(self):
        print("start creating rules")
        investor_role,_ = Role.objects.get_or_create(name=UserRoles.INVESTOR.value[0])
        for permission in UserRoles.permissions_for(UserRoles.INVESTOR.name):
            Permission.objects.get_or_create(name=permission[0], role=investor_role)
        print("finish creating rules")