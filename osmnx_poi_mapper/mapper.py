# osmnx_poi_mapper/mapper.py
import pandas as pd
import geopandas as gpd
import re


def read_categories(path: str) -> dict:
    """
    Reads a file containing OSM categories and returns a dictionary with the categories grouped by super-category.
    
    Args:
    - path (str): Path to the file containing OSM categories.
    
    Returns:
    - dict: A dictionary with categories grouped by super-category.
    """ 

    tags = {}

    with open(path) as f:

        lines = f.readlines()

        tag = ""

        for line in lines:

            super_category = re.findall(r".*=",line)
            super_category = super_category[0][0:-1]

            category = re.findall(r"=.*;",line)
            category = category[0][1:-1]

            if tag == super_category:

                tags[tag].append(category)

            else:
                
                tag = super_category
                tags[tag] = []
                tags[tag].append(category)

    return tags


def map_poi_categories(poi_gdf: gpd.GeoDataFrame, category_dict: dict, tags: dict) -> gpd.GeoDataFrame:
    """
    Maps categories in a POI dataset to readable names based on a provided category mapping file.
    Categories not in the file will be replaced with the column name.

    Args:
    - poi_gdf (gpd.GeoDataFrame): A GeoDataFrame containing POIs.
    - category_dict (dict): A dictionary with categories grouped by super-category.
    - tags (dict): A dictionary with the tags used to filter POIs.

    Returns:
    - gpd.GeoDataFrame: A GeoDataFrame with mapped POI categories.
    """
    # Load POIs and category mapping
    pois = poi_gdf.copy()
    pois.reset_index(inplace=True)
        
    cols = list(tags.keys())
    
    pois = pois[cols+['osmid','geometry']]
    
    category_map = {}
    for group, items in category_dict.items():
        for item in items:
            category_map[item] = group
            
    for col in cols:
        pois[col] = pois[col].map(category_map)
        # fill missing values with the name of the column
        pois[col].fillna(col, inplace=True)
    
    pois['category'] = pois[cols].bfill(axis=1).iloc[:, 0]

    return pois[['osmid', 'category', 'geometry']]

