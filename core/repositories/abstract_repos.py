from abc import ABC, abstractmethod
from typing import Iterable


class Repository(ABC):

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
    def create[T](self, model: T) -> T:
        pass

    @abstractmethod
    def batch_create[T](self, models: Iterable[T]):
        pass

    @abstractmethod
    def update[T](self, model: T) -> T:
        pass

    @abstractmethod
    def batch_update[T](self, models: Iterable[T]) -> Iterable[T]:
        pass