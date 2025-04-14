from models.ports.analysis_repository import AnalysisRepository
from models.analysis.analysis import Analysis


class AnalysisController:
    def __init__(
        self,
        analysis_repository: AnalysisRepository,
    ):
        self.analysis_repository = analysis_repository

    def get_analysis_by_id(self, id: int) -> Analysis | None:
        return self.analysis_repository.get_analysis_by_id(id)
