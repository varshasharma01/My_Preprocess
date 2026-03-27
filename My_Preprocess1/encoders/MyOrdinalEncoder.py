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

    def __init__(self, order):
        self.order = order
        self.mapping = None
        self.most_frequent = None

    def fit(self, X):
        X = np.array(X).flatten()

        # create mapping
        self.mapping = {cat: i for i, cat in enumerate(self.order)}

        # find most frequent category
        X_series = pd.Series(X).dropna()
        most_frequent_category = X_series.mode()[0]

        self.most_frequent = self.mapping.get(most_frequent_category, 0)

        return self

    def transform(self, X):
        if self.mapping is None:
            raise ValueError("Call fit() before transform()")

        X = np.array(X).flatten()

        result = []
        for value in X:
            if pd.isna(value):
                result.append(self.most_frequent)
            elif value in self.mapping:
                result.append(self.mapping[value])
            else:
                result.append(self.most_frequent)

        return np.array(result).reshape(-1, 1)

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
         
# df = pd.read_csv("Practice/covid_data.csv")
# X = df['cough']

# oe = MyOrdinalEncoder()

# print(oe.ordinal_encoding(X))

