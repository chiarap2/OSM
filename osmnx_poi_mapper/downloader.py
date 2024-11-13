# osmnx_poi_mapper/downloader.py
import osmnx as ox
import geopandas as gpd

def download_pois(place_name: str, tags: dict) -> gpd.GeoDataFrame:
    """
    Downloads Points of Interest (POIs) for a given place using OSMnx.

    Args:
    - place_name (str): Name of the place (city, region, etc.)
    - tags (dict): List of OSM tags for filtering specific POIs.

    Returns:
    - gpd.GeoDataFrame: A GeoDataFrame containing POIs.
    """

    pois = ox.features_from_place(place_name, tags=tags)
    
    return pois
