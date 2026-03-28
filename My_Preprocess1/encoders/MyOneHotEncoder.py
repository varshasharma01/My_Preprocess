import numpy as np
import pandas as pd

class MyOneHotEncoder:

    def fit(self, X):
        self.X = np.array(X).flatten()
        self.categories = np.unique(self.X)

    def transform(self, X):
        X = np.array(X).flatten()

        result = {}
        for category in self.categories:
            result[category] = (X == category).astype(int)

        return pd.DataFrame(result).values
    
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


