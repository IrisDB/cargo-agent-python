from src.analyzer.base_analyzer import BaseAnalyzer
import logging


class VoidAnalyzer(BaseAnalyzer):

    def analyze(self, path: str) -> list:
        logging.warning("Falling back to the `void` analyzer!")
        return []
