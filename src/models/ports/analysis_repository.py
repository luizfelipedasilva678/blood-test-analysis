from abc import ABC, abstractmethod
from models.analysis.analysis import Analysis


class AnalysisRepository(ABC):
    @abstractmethod
    def get_analysis_by_id(self, id: int) -> Analysis | None:
        pass

    @abstractmethod
    def get_analysis_by_user_id(self, user_id: int) -> list:
        pass

    @abstractmethod
    def register(self, analysis: Analysis) -> None:
        pass
