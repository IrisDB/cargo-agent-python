import os.path
from unittest import TestCase
from src.analyzer.moving_pandas_trajectory_collection.analyzer import MovingPandasAnalyzer
from test.config.definitions import ROOT_DIR


class TestMovingPandasAnalyzer(TestCase):

    def setUp(self) -> None:
        self.sut = MovingPandasAnalyzer()

    def test_it_should_analyze_input1(self):
        # execute
        actual = self.sut.analyze(path=self.__test_file("input1.pickle"))

        # verify
        self.assertEqual(actual['animals_total_number'], 3)
        self.assertEqual(actual['animal_names'], ['Nemo blue', 'Nils yellow', 'Paula white'])
        self.assertEqual(actual['taxa'], ['Anser anser'])
        self.assertEqual(actual['track_names'], ['Nemo blue', 'Nils yellow', 'Paula white'])

    def test_it_should_analyze_input2(self):
        # execute
        actual = self.sut.analyze(path=self.__test_file("input2.pickle"))

        # verify
        self.assertEqual(actual['animals_total_number'], 3)
        self.assertEqual(actual['animal_names'], [742, 746, 749])
        self.assertEqual(actual['taxa'], ['Anser albifrons'])
        self.assertEqual(actual['track_names'], [742, 746, 749])

    def test_it_should_analyze_input3(self):
        # execute
        actual = self.sut.analyze(path=self.__test_file("input3.pickle"))

        # verify
        self.assertEqual(actual['animals_total_number'], 1)
        self.assertEqual(actual['animal_names'], ['Prinzesschen'])
        self.assertEqual(actual['taxa'], ['Ciconia ciconia'])
        self.assertEqual(actual['track_names'], ['Prinzesschen'])

    def test_it_should_analyze_input4(self):
        # execute
        actual = self.sut.analyze(path=self.__test_file("input4.pickle"))

        # verify
        self.assertEqual(actual['animals_total_number'], 1)
        self.assertEqual(actual['animal_names'], ['Goat-8810'])
        self.assertEqual(actual['taxa'], ['Capra hircus'])
        self.assertEqual(actual['track_names'], ['Goat-8810'])

    def __test_file(self, file_name) -> str:
        return os.path.join(ROOT_DIR, 'test', 'resources', 'moving_pandas_trajectory_collection', file_name)
