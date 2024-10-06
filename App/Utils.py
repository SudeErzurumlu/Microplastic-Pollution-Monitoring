import requests
from netCDF4 import Dataset

def get_modis_data():
    url = "MODIS_API_ENDPOINT"
    response = requests.get(url)
    return Dataset(response.content)

def get_sentinel_data():
    url = "SENTINEL_API_ENDPOINT"
    response = requests.get(url)
    return Dataset(response.content)

def get_cmems_data():
    url = "CMEMS_API_ENDPOINT"
    response = requests.get(url)
    return Dataset(response.content)
