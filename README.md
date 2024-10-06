# Microplastic Pollution Monitoring System

## Overview
Microplastic pollution in marine environments is a growing environmental issue, with plastics dispersing over wide areas of the ocean and affecting marine life. Traditional methods for tracking pollution are limited in scope, but satellite-based monitoring offers a scalable solution. This project leverages satellite data from **MODIS**, **Sentinel-2**, and **CMEMS** to detect and monitor microplastic pollution in the ocean.

The system automatically downloads satellite data, processes it to remove atmospheric and cloud artifacts, and uses spectral analysis to identify areas of high microplastic concentration. It provides real-time alerts for areas with significant pollution, enabling more targeted cleanup efforts.

## Features
- **Automated Data Retrieval**: Automatically fetches satellite data from NASA Earthdata, Copernicus Sentinel, and Copernicus Marine Service.
- **Real-time Pollution Detection**: Processes data and generates alerts for high-pollution areas.
- **Visualization**: Displays a pollution heatmap showing the distribution and intensity of microplastic pollution.
- **Modular Code**: Easily adaptable for other types of environmental monitoring.

## Data Sources and Access
Three main satellite data sources are used in this project:

1. **MODIS (Moderate Resolution Imaging Spectroradiometer)**:
   - **Purpose**: Provides Sea Surface Temperature (SST) data.
   - **Source**: [NASA Earthdata MODIS](https://www.earthdata.nasa.gov/sensors/modis)
   - **API Access**: Register for a NASA Earthdata account and obtain API credentials from the [LAADS DAAC platform](https://ladsweb.modaps.eosdis.nasa.gov/). API keys are required to automate data download.

2. **Sentinel-2**:
   - **Purpose**: High-resolution optical imagery for detecting microplastics and tracking their spread.
   - **Source**: [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-2)
   - **API Access**: Create an account on the Copernicus Data Space Ecosystem, and follow the [Sentinel-2 API guide](https://sentinelsat.readthedocs.io/en/stable/) to access data.

3. **CMEMS (Copernicus Marine Environment Monitoring Service)**:
   - **Purpose**: Provides ocean surface data and current patterns to model the movement of microplastics.
   - **Source**: [Copernicus Marine Service](https://data.marine.copernicus.eu/products)
   - **API Access**: Sign up for a CMEMS account and follow the [CMEMS API documentation](https://marine.copernicus.eu/faq/how-access-our-fptnciproducts/) to acquire necessary API keys.

## Technical Details
The system utilizes a combination of Python libraries and frameworks for data retrieval, processing, and visualization:
- **Streamlit**: A web framework for interactive data applications.
- **Numpy** and **Rasterio**: For numerical operations and satellite imagery processing.
- **Scikit-Learn**: For clustering and classification.
- **Matplotlib**: For generating pollution heatmaps.

### Spectral Signature Analysis
The system uses Sentinel-2’s optical bands to detect plastic pollution based on their unique spectral signatures. Specifically, the algorithm focuses on infrared and visible light bands to distinguish between microplastics and other materials.

### Data Cleaning
- **Atmospheric Correction**: Removes distortions caused by atmospheric particles.
- **Cloud Masking**: Filters out areas covered by clouds to ensure accurate readings.
- **Alignment**: Aligns data from MODIS, Sentinel-2, and CMEMS to analyze areas of overlap for pollution detection.

## Installation and Setup

### Prerequisites
- **Python 3.7+**: Ensure you have Python installed on your machine.
- **API Credentials**: Register on each data provider’s platform and obtain API keys for automated data retrieval.

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Microplastic-Pollution-Monitoring.git
   cd Microplastic-Pollution-Monitoring

2. **Install Dependencies**:
   * Use the provided requirements.txt file to install necessary Python libraries.
   ```bash
   pip install -r requirements.txt


3. **Configure API Keys**:
  * In the project directory, create a .env file with the following structure:
   ```bash
  MODIS_API_KEY=your_modis_api_key
  SENTINEL_API_KEY=your_sentinel_api_key
  CMEMS_API_KEY=your_cmems_api_key
  * Replace your_modis_api_key, your_sentinel_api_key, and your_cmems_api_key with your actual API key
```

### Running the Application
To start the application, use the following command:

```bash
streamlit run app/microplastic_app.py

### Usage
- **Data Retrieval**: The application will automatically download the latest MODIS, Sentinel-2, and CMEMS data using the provided API keys.
- **Data Processing**: The downloaded data is processed to remove atmospheric distortions and clouds. Then, spectral analysis is performed to identify microplastic pollution.
- **Pollution Heatmap**: A heatmap of microplastic concentration is displayed on the main interface. Areas with high pollution levels are highlighted.
- **Alerts**: If the system detects significant pollution levels, an alert will appear on the interface.
