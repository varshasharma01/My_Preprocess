from .encoders.MyLabelEncoder import MyLabelEncoder
from .encoders.MyOneHotEncoder import MyOneHotEncoder
from .encoders.MyOrdinalEncoder import MyOrdinalEncoder
from .my_pipeline import MyPipeline

import numpy as np
import pandas as pd

class MyColumnTransformer:

    def __init__(self, transformers):
        self.transformers = transformers

    def fit_transform(self, df):
        outputs = []

        for name, encoder, col in self.transformers:
            
            # it will extract column data
            data = df[col]
            # data = np.array(data).reshape(-1, 1)
            transformed = encoder.fit_transform(data)

            outputs.append(transformed)

        # this will combine all outputs
        return np.concatenate(outputs, axis=1)


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

