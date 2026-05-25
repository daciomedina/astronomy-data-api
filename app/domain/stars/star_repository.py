from abc import ABC, abstractmethod

from app.domain.stars.star import Star


class StarRepository(ABC):
    @abstractmethod
    def find_nearest(self, limit: int = 10) -> list[Star]:
        pass

    @abstractmethod
    def find_by_id(self, star_id: str) -> Star | None:
        pass
