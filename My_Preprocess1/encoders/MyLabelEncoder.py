import numpy as np
import pandas as pd

class MyLabelEncoder:

    def fit(self, y):
        y = np.array(y).flatten()

        self.categories = np.unique(y[~pd.isna(y)])

        # most frequent (for missing values)
        y_series = pd.Series(y).dropna()
        self.most_frequent = y_series.mode()[0]

        self.mapping = {val: idx for idx, val in enumerate(self.categories)}

        return self

    def transform(self, y):
        y = np.array(y).flatten()

        result = []
        for val in y:
            if pd.isna(val):
                # handle missing value
                result.append(self.mapping[self.most_frequent])

            elif val in self.mapping:
                result.append(self.mapping[val])

            else:
                # unseen category
                result.append(self.mapping[self.most_frequent])

        return np.array(result).reshape(-1, 1)

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)
# df = pd.read_csv("Practice/covid_data.csv")
# y = df['has_covid']

# le = MyLabelEncoder()
# print(le.fit_transform(y))