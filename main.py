# main.py
import json
from osmnx_poi_mapper.downloader import download_pois
from osmnx_poi_mapper.mapper import map_poi_categories, read_categories
from osmnx_poi_mapper.utils import save_parquet



def read_config(config_path):
    with open(config_path) as f:
        return json.load(f)

def main():
    # Step 1: Download POIs for a specific location
    config = read_config('config.json')
    place_name = config["place_name"]
    poi_tags = config["poi_tags"]
    
    pois = download_pois(place_name, poi_tags)
    
    # Step 2: Process and map categories in the POI data
    tags = read_categories('data/pois_categories_OSM.txt')

    pois_with_mapped_categories = map_poi_categories(pois, tags, poi_tags)
    
    print(pois_with_mapped_categories['category'].unique())
    # Step 3: Save processed data
    save_parquet(pois_with_mapped_categories, f'pois_mapped_{place_name[0:place_name.index(',')].lower()}.parquet')

if __name__ == "__main__":
    main()
