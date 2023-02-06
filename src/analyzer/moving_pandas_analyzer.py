from src.analyzer.base_analyzer import BaseAnalyzer

import pandas as pd
import geopandas as gpd
import movingpandas as mpd
import logging


class MovingPandasAnalyzer(BaseAnalyzer):

    def analyze(self, path: str) -> dict:
        movingpandas = self.__read(path=path)
        geopandas = self.__convert(movingpandas=movingpandas)
        return self.__inspect(data=geopandas)

    def __read(self, path: str) -> mpd.TrajectoryCollection:
        movingpandas = pd.read_pickle(path)
        logging.info(f'read movingpandas: {movingpandas}')
        return movingpandas

    def __convert(self, movingpandas: mpd.TrajectoryCollection) -> gpd.GeoDataFrame:
        geopandas = movingpandas.to_point_gdf()
        print(f'From {type(movingpandas)} to {type(geopandas)}')
        logging.info(geopandas.info())
        logging.info(geopandas.head())
        return geopandas

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
