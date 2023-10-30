from typing import override

from core.models import Task
from core.repositories.abstract_repos import CRUDRepo


class TaskRepo(CRUDRepo):
    @override
    def __init__(
        self,
    ):
        super().__init__(Task)

    @override
    def get(self, pk):
        return (
            self.model.objects.filter(id=pk).select_related("owner", "feature").first()
        )
