from copy import deepcopy
from typing import override

from django.db import transaction

from core.repositories.abstract_repos import CRUDRepo


class UserRepo(CRUDRepo):

    @override
    @transaction.atomic
    def update(self, pk, **kwargs):
        instance = None

        if 'password' in kwargs:
            password = deepcopy(kwargs['password'])
            del kwargs['password']
            instance = self.model.objects.filter(id=pk).first()
            instance.set_password(password)

        instance.update(**kwargs)
