from abc import ABC, abstractmethod
from typing import Iterable


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
    def batch_delete(self, pks: list):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def batch_create[T](self, instances: Iterable[T]):
        pass

    @abstractmethod
    def update[T](self, instance: T) -> T:
        pass

    @abstractmethod
    def batch_update[T](self, instances: Iterable[T]) -> Iterable[T]:
        pass