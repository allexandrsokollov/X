from typing import Iterable, override

from core.exceptions.repository_exceptions import NotFoundException
from core.models import User
from core.repositories.abstract_repos import Repository


class UserRepo(Repository):

    @override
    def __init__(self):
        self.model = User

    @override
    def get_all(self) -> Iterable[User]:
        objects = self.model.objects.all()

        return objects

    @override
    def get(self, pk) -> User | None:
        return self.model.objects.filter(id=pk).first()

    @override
    def create(self, **kwargs) -> User:
        created = self.model.objects.create(**kwargs)
        return created


    @override
    def delete(self, pk):
        user = self.model.objects.filter(id=pk)
        if not user:
            raise NotFoundException(f'user with this pk: {pk} not found')
        user.delete()

    @override
    def update(self,pk,  **kwargs):
        User.objects.update(id=pk, **kwargs)
