# main.py
from osmnx_poi_mapper.downloader import download_pois
from osmnx_poi_mapper.mapper import map_poi_categories, read_categories
from osmnx_poi_mapper.utils import save_parquet

def main():
    # Step 1: Download POIs for a specific location
    place_name = 'Manhattan, New York, USA'  # Example place
    poi_tags = {'amenity': True}  # Example tags
    
    pois = download_pois(place_name, poi_tags)

    # Step 2: Process and map categories in the POI data
    tags = read_categories('data/pois_categories_OSM.txt')
    pois_with_mapped_categories = map_poi_categories(pois, tags, poi_tags)

    # Step 3: Save processed data
    save_parquet(pois_with_mapped_categories, f'pois_mapped_{place_name[0:place_name.index(',')].lower()}.parquet')

if __name__ == "__main__":
    main()
