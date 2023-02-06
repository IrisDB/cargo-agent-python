from movingpandas import TrajectoryCollection
import pandas as pd
import geopandas as gpd
import movingpandas as mpd
import logging


class MovingPandasAnalyzer:

    def analyze(self, path: str) -> dict:
        movingpandas = self.read(path=path)
        geopandas = self.convert(movingpandas=movingpandas)
        return self.inspect(data=geopandas)

    def read(self, path: str) -> mpd.TrajectoryCollection:
        movingpandas = pd.read_pickle(path)
        logging.info(f'read movingpandas: {movingpandas}')
        return movingpandas

    def convert(self, movingpandas: mpd.TrajectoryCollection) -> gpd.GeoDataFrame:
        geopandas = movingpandas.to_point_gdf()
        print(f'From {type(movingpandas)} to {type(geopandas)}')
        logging.info(geopandas.info())
        logging.info(geopandas.head())
        return geopandas

    def inspect(self, data: gpd.GeoDataFrame) -> dict:
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
