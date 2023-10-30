from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        if not kwargs['username']:
            raise ValueError(gettext_lazy("The Email must be set"))

        if not kwargs['password']:
            raise ValueError(gettext_lazy("The password must be set"))

        user = self.model(**kwargs)
        user.set_password(kwargs['password'])
        user.save()

        return user

    def create_superuser(self, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if not kwargs.get("is_staff"):
            raise ValueError(gettext_lazy("Superuser must have is_staff=True"))
        if not kwargs.get("is_superuser"):
            raise ValueError(gettext_lazy("Superuser must have is_superuser=True"))

        return self.create_user(**kwargs)
