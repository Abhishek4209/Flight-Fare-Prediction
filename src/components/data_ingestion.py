import numpy as np
import pandas as pd
import os 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import sys





@dataclass
class Dataingenstionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=Dataingenstionconfig()
        
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method is started')
        
        try:
            df=pd.read_csv(os.path.join('notebook/data','Insurance.csv'))
            logging.info('Dataset read as Pandas DataFrame')
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path,index=False))
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            
            logging.info('Train test split')
            
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info('Ingestion of Data is Completed')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                
            )
            
        except Exception as e:
            logging.info('Error Occured in Data Ingestion Class')
            