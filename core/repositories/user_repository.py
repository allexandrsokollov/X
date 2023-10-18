from typing import Iterable, override

from core.models import User
from core.repositories.abstract_repos import Repository


class UserRepo(Repository):

    @override
    def __init__(self):
        self.model = User

    @override
    def get_all[T](self) -> Iterable[User]:
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
    def batch_create[T](self, instances: Iterable[T]):
        pass

    @override
    def delete(self, pk):
        pass

    @override
    def batch_delete(self, pks: list):
        pass

    @override
    def update[T](self, instance: T) -> T:
        pass

    @override
    def batch_update[T](self, instances: Iterable[T]) -> Iterable[T]:
        pass