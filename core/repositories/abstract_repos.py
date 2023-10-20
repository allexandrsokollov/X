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
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, pk, **kwargs):
        pass
