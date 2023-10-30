from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(gettext_lazy("The Email must be set"))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(gettext_lazy("Superuser must have is_staff=True"))
        if not extra_fields.get("is_superuser"):
            raise ValueError(gettext_lazy("Superuser must have is_superuser=True"))

        return self.create_user(username, password, **extra_fields)
