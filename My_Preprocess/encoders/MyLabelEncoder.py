import numpy as np
import pandas as pd

class MyLabelEncoder:

    def fit(self, y):
        self.categories = np.unique(y)

    def transform(self, y):
        mapping_value ={val: index for index,val in enumerate(self.categories)} 
        return y.map(mapping_value)
    
    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)
            

# df = pd.read_csv("Practice/covid_data.csv")
# y = df['has_covid']

# le = MyLabelEncoder()
# print(le.fit_transform(y))