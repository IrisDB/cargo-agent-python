from movingpandas import TrajectoryCollection
import pandas as pd


class MovingPandasAnalyzer:

    def analyze(self, path: str) -> dict:
        pandas = pd.read_pickle(path)
        print(pandas)

        return None
