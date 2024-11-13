# osmnx_poi_mapper/utils.py
import geopandas as gpd

def save_parquet(gdf: gpd.GeoDataFrame, filename: str):
    """
    Save a GeoDataFrame to a parquet file.
    """
    gdf.to_parquet(filename)
