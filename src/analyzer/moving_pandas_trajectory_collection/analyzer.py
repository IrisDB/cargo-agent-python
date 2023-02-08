from geopandas import GeoDataFrame

from src.analyzer.base_analyzer import BaseAnalyzer

import pandas as pd
import geopandas as gpd
import movingpandas as mpd
import logging


class MovingPandasAnalyzer(BaseAnalyzer):

    def analyze(self, path: str) -> dict:
        movingpandas = self.__read(path=path)
        geopandas = self.__convert(movingpandas=movingpandas)
        if geopandas is not None:
            return self.__inspect(data=geopandas)
        else:
            return {
                "animals_total_number": 0
            }

    def __read(self, path: str) -> mpd.TrajectoryCollection:
        movingpandas = pd.read_pickle(path)
        logging.info(f'read movingpandas: {movingpandas}')
        return movingpandas

    def __convert(self, movingpandas: mpd.TrajectoryCollection) -> GeoDataFrame | None:
        if len(movingpandas.trajectories) > 0:
            # Converting to geopandas is only possible if at least 1 trajectory is present"
            geopandas = movingpandas.to_point_gdf()
            print(f'From {type(movingpandas)} to {type(geopandas)}')
            logging.info(geopandas.info())
            logging.info(geopandas.head())
            return geopandas
        else:
            return None

    def __inspect(self, data: gpd.GeoDataFrame) -> dict:
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
            "animals_total_number": len(ids),
            "animal_names": names,
            "taxa": taxa,
            "track_names": ids
        }
