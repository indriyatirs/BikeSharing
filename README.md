# Bike Sharing System - Dicoding Final Project Data Analytics

This content is written to complete the final project of Dicoding's 'Belajar Analisis Data dengan Python' course and is used to explore, analyze, and create dashboards from data related to a bike sharing system. The content consists of two main files: a notebook file containing the analysis process of Data Wrangling, Exploratory Data Analysis, and Data Visualization; a Python file containing the dashboard using streamlit. The dashboard in this project can be accessed in [here](https://bikeshare-dashboard.streamlit.app/) or at the link https://bikeshare-dashboard.streamlit.app.

## Run `bike_sharing.ipynb` File
You can run the file by following these steps:
1. Download the `bike_sharing.ipynb` file.
2. You can use your favorite IDE like Jupyter Notebook or Google Colaboratory, but in here I use Google Colaboratory to run the file.
3. Upload and select the `bike_sharing.ipynb` file.
4. Click the `Connect` button at the top right corner to connect to a hosted runtime.
5. And then you can choose `Runtime` and run all the code cells.

## Run Streamlit App
You can run the dashboard file by following these steps:
1. Download the dashboard folder. Please note that you cannot move files within a dashboard folder as it may change the path within the `dashboard.py` file. 
2. Install the Streamlit in your terminal or command prompt using:
   ```
   pip install streamlit
   ```
3. Install another libraries like pandas, numpy, scipy, also matplotlib, seaborn, plotly.express, and plotly.graph_objects for visualization in this dashboard if you haven't.
4. You can load and read the `dashboard.py` file using VSCode.
5. Run the dashboard by using terminal in VSCode or command prompt and write the command:
   ```
   streamlit run dashboard.py
   ```
   or 
   ```
   python -m streamlit run dashboard.py
   ```

## Questions Explored
The content is answers the following questions about the bike sharing system dataset:
1. How is the user growth performance of the bike-sharing system?
2. When are the days that have the highest level of users?
3. When is the season with the highest percentage of users?
4. When is the highest number of bike rentals hours?
   
## Overview of Data Analysis Pipeline
### 1. Data collection: 
 - Used data from bike-sharing-dataset that contains information about bike rentals data from 2011 to 2012.

### 2. Data cleaning and preprocessing: 
 - Change mismatched data types and rename ambiguous columns.

### 3. Exploratory Data Analysis (EDA): 
 - Explore the `day_df` and `hour_df` data 

### 4. Data Visualization and Explanatory Analysis: 
 - Create a line charts with month and number of users by year and user type (casual and registered users).
 - Create multiple bar and line charts to compare total of casual and registered users in a week.
 - Create pie charts about seasonal and weather data.
 - Create line charts to see the level of bike rental users over 24 hours.
