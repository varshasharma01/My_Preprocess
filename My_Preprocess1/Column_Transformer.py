from .encoders.MyLabelEncoder import MyLabelEncoder
from .encoders.MyOneHotEncoder import MyOneHotEncoder
from .encoders.MyOrdinalEncoder import MyOrdinalEncoder
from .my_pipeline import MyPipeline

import numpy as np
import pandas as pd


class MyColumnTransformer:

    def __init__(self, transformers):
        self.transformers = transformers
        self.fitted_transformers = []

    def fit(self, df):
        self.fitted_transformers = []

        for name, encoder, col in self.transformers:
            
            data = df[col].values.reshape(-1, 1)

            # fit only
            encoder.fit(data)

            # store fitted encoder
            self.fitted_transformers.append((name, encoder, col))

        return self

    def transform(self, df):
        outputs = []

        for name, encoder, col in self.fitted_transformers:
            
            data = df[col].values.reshape(-1, 1)

            transformed = encoder.transform(data)

            #  ensure 2D
            if len(transformed.shape) == 1:
                transformed = transformed.reshape(-1, 1)

            outputs.append(transformed)

        return np.concatenate(outputs, axis=1)

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)

# df = pd.read_csv("Practice/SalaryData.csv")

# ct = MyColumnTransformer([
#     # ("label", MyLabelEncoder(), "cough"),
#     ("ordinal", MyOneHotEncoder(), "Education Level")
#     # ("onehot", MyOneHotEncoder(), "city")
# ])


# result = ct.fit_transform(df)
# print(result) 


# ct = MyColumnTransformer([

#     ("education_pipe",
#      MyPipeline([
#          ("ordinal", MyOrdinalEncoder())
#      ]),
#      "Education Level"
#     ),

#     ("gender_pipe",
#      MyPipeline([
#          ("onehot", MyOneHotEncoder())
#      ]),
#      "Gender"
#     )])

