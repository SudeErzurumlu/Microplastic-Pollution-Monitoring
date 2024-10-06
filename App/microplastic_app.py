import streamlit as st
import numpy as np
import rasterio
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import requests
from netCDF4 import Dataset
from utils import get_modis_data, get_sentinel_data, get_cmems_data

st.title("Microplastic Pollution Monitoring System")
st.write("Monitor marine pollution using satellite data from MODIS, Sentinel-2, and CMEMS.")

modis_data = get_modis_data()
sentinel_data = get_sentinel_data()
cmems_data = get_cmems_data()

# Function to Process Data
def process_data(modis_data, sentinel_data, cmems_data):
    cloud_mask = sentinel_data[1] < 3000
    sentinel_data[1][~cloud_mask] = np.nan

    reshaped_data = sentinel_data.reshape(-1, sentinel_data.shape[0])
    kmeans = KMeans(n_clusters=2)
    labels = kmeans.fit_predict(reshaped_data)
    return labels.reshape(sentinel_data.shape[1:])

pollution_map = process_data(modis_data, sentinel_data, cmems_data)

# Visualization and Alerts
plt.imshow(pollution_map, cmap='coolwarm')
plt.colorbar(label='Pollution Level')
plt.title("Microplastic Pollution Map")
st.pyplot()

if np.any(pollution_map):
    st.warning("High microplastic pollution detected!")
else:
    st.success("No significant pollution detected.")
