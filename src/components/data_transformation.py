import os 
import numpy as np
import pandas as pd
import seaborn as sns
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler,RobustScaler
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass




## Data Transformation config
@dataclass
class DataTransformationConfig():
    def __init__(self):
        preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")




## Data Transformation class:-

class DataTransformation:
    def __init__(self):
        self.datatransformetion=DataTransformationConfig()
        
    def get_data_transformation_object(self):
        try:
            logging.info("Data Transformation is Started")
            
            
            
            
            
        
        
        
        except Exception as e:
            logging.info("Data Transformation Class is Not Succesfully Done")
            raise CustomException(e,sys)
        