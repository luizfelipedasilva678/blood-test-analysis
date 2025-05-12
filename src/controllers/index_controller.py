from models.ports.analysis_repository import AnalysisRepository
from models.analysis.analysis import Analysis
from models.ports.bloodtest_analyzer import BloodTestAnalyzer
from re import search, IGNORECASE


class IndexController:
    def __init__(
        self,
        analysis_repository: AnalysisRepository,
        bloodtest_analyzer: BloodTestAnalyzer,
    ):
        self.analysis_repository = analysis_repository
        self.bloodtest_analyzer = bloodtest_analyzer

    def get_analysis_by_user_id(self, user_id: int) -> list:
        return self.analysis_repository.get_analysis_by_user_id(user_id)

    def register(self, title, image, user_id) -> bool:
        try:
            analysis_result = self.bloodtest_analyzer.analyze(image)

            if search(".*error.*", analysis_result, IGNORECASE):
                return False

            self.analysis_repository.register(
                Analysis(title, self.bloodtest_analyzer.analyze(image), user_id)
            )

            return True
        except Exception as e:
            return False
