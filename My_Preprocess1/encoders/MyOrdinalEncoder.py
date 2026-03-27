# import numpy as np 
# import pandas as pd

# class MyOrdinalEncoder:
    
#     # def ordinal_encoding(self, X):
        
    #     order = {
    #         "Strong": 1,
    #         "Mild": 0
    #     }
    #     #   we can use for loop but this is faster to do
    #     return X.map(order)
    
import numpy as np
import pandas as pd

class MyOrdinalEncoder:

    def __init__(self):
        self.mapping = None
        self.most_frequent = None

    def fit(self, X, order):
        self.mapping = {}
        for i, category in enumerate(order):
            self.mapping[category] = i

        # Convert to pandas Series to easily drop NaN and find mode
        X_series = pd.Series(X).dropna()
        most_frequent_category = X_series.mode()[0]  # mode() returns sorted Series, take first
        self.most_frequent = self.mapping.get(most_frequent_category, 0)

        return self

    def transform(self, X):
        if self.mapping is None:
            raise ValueError("Call fit() before transform()")

        X_array = np.array(X)  # convert to numpy array

        result = []
        for value in X_array:
            # check for NaN using pandas (works for both str and float NaN)
            if pd.isna(value):
                result.append(self.most_frequent)   # fill NaN with mode
            elif value in self.mapping:
                result.append(self.mapping[value])
            else:
                result.append(self.most_frequent)   # fill unseen category with mode

        return np.array(result).reshape(-1, 1)

    def fit_transform(self, X, order):
        self.fit(X, order)
        return self.transform(X)  
         
# df = pd.read_csv("Practice/covid_data.csv")
# X = df['cough']

# oe = MyOrdinalEncoder()

# print(oe.ordinal_encoding(X))

