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
        self.mapping = None
        
    def fit(self,X, order):
        self.mapping = {}
        
        for i, category in enumerate(order):
            self.mapping[category] = i
            
        self.mapping = self.mapping
        return self

    
    def transform(self, X):
        if self.mapping is None:
            raise ValueError("first insert the order")
        
        result = []
        for value in X:
            if value in self.mapping is None:
                result.append(self.mapping[value])
                
            else:
                result.append(-1)
     
        return np.array(result).reshape(-1, 1)
    
    def fit_transform(self, X, order):
        self.fit(X,order)
        return self.transform(X)  
    
         
# df = pd.read_csv("Practice/covid_data.csv")
# X = df['cough']

# oe = MyOrdinalEncoder()

# print(oe.ordinal_encoding(X))

