from src.analyzer.base_analyzer import BaseAnalyzer


class VoidAnalyzer(BaseAnalyzer):

    def analyze(self, path: str) -> dict:
        return {}
