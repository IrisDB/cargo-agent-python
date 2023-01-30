from movingpandas import TrajectoryCollection
import pandas as pd
import logging


class MovingPandasAnalyzer:

    def read(self, path: str) -> pd.DataFrame:
        pandas = pd.read_pickle(path)
        logging.info(pandas.info())
        return pandas

    def analyze(self, data: pd.DataFrame) -> dict:
        ids = data['individual.local.identifier'].unique().tolist()
        if 'individual.local.identifier' in data:
            names = data['individual.local.identifier'].unique().tolist()
        else:
            names = "no appropriate animal names available"
        if 'individual.taxon.canonical.name' in data:
            taxa = data['individual.taxon.canonical.name'].unique().tolist()
        else:
            taxa = "no appropriate taxa names available"

        return {
            "animal_names": names,
            "taxa": taxa,
            "track_names": ids
        }
