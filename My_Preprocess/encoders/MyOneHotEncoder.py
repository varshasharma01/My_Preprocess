import numpy as np
import pandas as pd

class MyOneHotEncoder:

    def fit(self, X):
        self.categories = np.unique(X.dropna())

    def transform(self, X):
    
        result = {}
    
        for category in self.categories:
            # for this category, compare every value in X
            # convert True-False to 1-0
            # store in result dictionary with category as key
            result[category] = (X == category).astype(int)
        
        # convert dictionary to DataFrame and return
        return pd.DataFrame(result)

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

# df = pd.read_csv("Practice/covid_data.csv")
# X = np.array(df['gender']).reshape(-1,1)

# X = [['male']], [['female']]
# df = pd.read_csv("Practice/SalaryData.csv")
# X = df['Education Level']


# print(type(X))
# ohe = MyOneHotEncoder()
# print(ohe.fit_transform(X))


