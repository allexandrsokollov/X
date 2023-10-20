from abc import ABC, abstractmethod
from typing import Iterable, override

from core.exceptions.repository_exceptions import NotFoundException


class Repository(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all[T](self, filters: dict[str, T]) -> Iterable[T]:
        pass

    @abstractmethod
    def get(self, pk):
        pass

    @abstractmethod
    def delete(self, pk):
        pass


    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, pk, **kwargs):
        pass


class CRUDRepo(Repository):
    def __init__(self, model_class):
        self.model = model_class

    @override
    def get_all(self) -> Iterable:
        objects = self.model.objects.all()

        return objects

    @override
    def get(self, pk):
        return self.model.objects.filter(id=pk).first()

    @override
    def create(self, **kwargs):
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
        self.model.objects.update(id=pk, **kwargs)