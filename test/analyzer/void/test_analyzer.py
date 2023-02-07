from unittest import TestCase
from src.analyzer.void.analyzer import VoidAnalyzer


class TestMovingPandasAnalyzer(TestCase):

    def setUp(self) -> None:
        self.sut = VoidAnalyzer()

    def test_it_should_analyze_nothing(self):
        # execute
        actual = self.sut.analyze(path="any")

        # verify
        self.assertEqual(len(actual), 0)
