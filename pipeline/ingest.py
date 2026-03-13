'''
import pandas as pd

def load_raw_file(file_path):
    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    return df 
'''

import geopandas as gpd

def load_geojson(file_path):
    gdf = gpd.read_file(file_path)
    return gdf
