from typing import Iterable

from core.repositories.abstract_repos import Repository


class ProjectRepo(Repository):
    def __init__(self):
        self.mol

    def get_all(self, filters: dict[str, T]) -> Iterable[T]:
        pass

    def get(self, pk):
        pass

    def delete(self, pk):
        pass

    def create(self, **kwargs):
        pass

    def update(self, pk, **kwargs):
        pass