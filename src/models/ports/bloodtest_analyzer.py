from abc import ABC, abstractmethod


class BloodTestAnalyzer(ABC):
    @abstractmethod
    def analyze(self, image) -> str:
        pass
