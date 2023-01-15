# ID2223 Project - Air quality

The repository contains the code for the Air Quality project in which you are able to predict air quality of the coming week, this model is based on London and its historic data. The air quality is calculated with past air quality and weather data and then the model calculates the AQI from future weather. In general, a higher AQI corresponds to unhealthy and polluted air while a lower corresponds to the opposite.

## Description of the code

The code used in the project is based on the Air Quality Prediction tutorial from Hopsworks: https://github.com/logicalclocks/hopsworks-tutorials/tree/master/advanced_tutorials/air_quality

1. Backfill_feature_groups.py parses historical weather and air quality data and creates feature groups on Hopsworks.
2. Feature_pipeline.py creates the feature pipelines and uploads daily data (both weather and air quality).
3. Feature_views_and_training_dataset.py combines the feature pipelines into a feature view and creates a training pipeline.
4. Model_training.py trains the model with a Gradient Boosting Regressor.
Finally, a UI is created on Hugging Face to illustrate the coming weeks predicted air quality.

## Data sources 

Historic weather data was collected from https://www.visualcrossing.com/ while the historic air quality data was collected from https://aqicn.org//here/

## Hugging Face UI

The finished Hugging Face UI can be accessed here (enter a random input): https://huggingface.co/spaces/freeja/Air-Quality
