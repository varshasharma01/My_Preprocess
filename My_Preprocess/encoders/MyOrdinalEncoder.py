import numpy as np 
import pandas as pd

class MyOrdinalEncoder:
    
    # def ordinal_encoding(self, X):
        
    #     order = {
    #         "Strong": 1,
    #         "Mild": 0
    #     }
    #     #   we can use for loop but this is faster to do
    #     return X.map(order)
    
    def __init__(self):
        pass
        
    def fit(self,X):
        order = {
            "Strong": 1,
            "Mild": 0
        }    
        return order
    
    def transform(self, X):
        order = {
            "Strong": 1,
            "Mild": 0
        }
        
        return X.map(order).values.reshape(-1, 1)
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)  
    
         
# df = pd.read_csv("Practice/covid_data.csv")
# X = df['cough']

# oe = MyOrdinalEncoder()

# print(oe.ordinal_encoding(X))

