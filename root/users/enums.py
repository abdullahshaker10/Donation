import enum


class UserRoles(enum.Enum):
    ADMIN = (
        "Admin",
        [
            ("can_view", "Can view"),
            ("can_edit", "Can edit"),
            ("can_delete", "Can delete"),
        ],
    )
    DONAR = "Donar", [("can_view", "Can view"), ("can_donate", "Can donate")]
    ORGANIZER = "Organizer", [("can_view", "Can view"), ("can_create", "Can create")]

    @classmethod
    def value_name_choices(cls):
        return [(role.value[0], role.name) for role in cls]

    @classmethod
    def permissions_for(cls, role_name):
        """Retrieve permissions for a specific role."""
        for role in cls:
            if role.name == role_name:
                return role.value[1]
        return []

    @classmethod
    def all_permissions(cls):
        """Return a flat list of all unique permissions."""
        permissions = []
        for role in cls:
            permissions.extend(role.value[1])  # Add each role's permissions
        return permissions
