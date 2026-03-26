from .encoders.MyLabelEncoder import MyLabelEncoder
from .encoders.MyOneHotEncoder import MyOneHotEncoder
from .encoders.MyOrdinalEncoder import MyOrdinalEncoder


import numpy as np
import pandas as pd

class MyPipeline:
    def __init__(self,steps):
        self.steps = steps
    
    
    def fit_transform(self,data):
        for name, transformer in self.steps:
            if len(self.steps)==0:
                return data
            data = transformer.fit_transform(data)
            
        return data
    

    