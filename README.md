# 📌 My Preprocess Library

A custom data preprocessing library built from scratch using NumPy and pandas.  
This project includes a Column Transformer, multiple encoders, a custom Pipeline, and Standard Scaling — inspired by scikit-learn.

---
##  Installation

pip install varsha-preprocess==0.2.1

---

## 🚀 Overview

This project recreates core preprocessing components without using any ML libraries. List of students scoring 95 % and above marks in Secondary Examination of students scoring 95 % and above marks in Secondary Examination

Includes:
- Column Transformer
- Label Encoding
- Ordinal Encoding
- One Hot Encoding
- Custom Pipeline
- Standard Scaling

---

## ✨ Features

- Built completely from scratch
- Uses only NumPy and pandas
- Modular and reusable design
- Column-wise transformations
- Sequential pipeline support
- Easy to extend

---

## 🏗️ Project Structure

```
My_Preprocess/
│
├── column_transformer.py
├── mypipeline.py
├── standardscaling.py
├── encoders/
│   ├── MyLabelEncoder.py
│   ├── MyOrdinalEncoder.py
│   └── MyOneHotEncoder.py
├── preprocessing/
│   └── my_scaler.py
└── Practice/
    └── covid_data.csv
```

---

## ⚙️ To Clone

```bash
git clone https://github.com/varshasharma01/My_Preprocess.git
cd My_Preprocess
```

---

## 📊 Usage

### 🔹 Column Transformer

```python
from column_transformer import MyColumnTransformer
from encoders.MyLabelEncoder import MyLabelEncoder
from encoders.MyOrdinalEncoder import MyOrdinalEncoder
from encoders.MyOneHotEncoder import MyOneHotEncoder
import pandas as pd

df = pd.read_csv("Practice/covid_data.csv")

ct = MyColumnTransformer([
    ("label", MyLabelEncoder(), "cough"),
    ("ordinal", MyOrdinalEncoder(), "fever"),
    ("onehot", MyOneHotEncoder(), "city")
])

result = ct.fit_transform(df)
print(result)
```

---

### 🔹 Pipeline

```python
from mypipeline import MyPipeline
from standardscaling import standardscaling

pipeline = MyPipeline([
    ("scaler", standardscaling())
])

result = pipeline.fit_transform(data)
```

---

### 🔹 Standard Scaling

```python
from standardscaling import standardscaling

scaler = standardscaling()

scaled_data = scaler.fit_transform(data)
```

---

## 📌 Example

### Input

```
cough   fever   city
Mild    High    Delhi
Strong  Low     Mumbai
```

### Output (example)

```
[[0 1 0 0 1]
 [1 0 1 0 0]]
```

---

## 🧩 Design

- Each transformer follows:
  - fit()
  - transform()
  - fit_transform()

- ColumnTransformer:
  - Applies transformations column-wise
  - Combines outputs using NumPy

- Pipeline:
  - Applies transformations sequentially
  - Passes output of one step to next

- StandardScaler:
  - Implements Z-score normalization

---

## 📈 Future Improvements

- Add remainder='passthrough'
- Support column indices + names
- Combine ColumnTransformer + Pipeline
- Handle missing values
- Add more scalers (MinMaxScaler)

---

## 🎯 Learning Outcomes

- Understood preprocessing internals
- Built ColumnTransformer from scratch
- Designed custom Pipeline system
- Implemented scaling mathematically
- Improved modular coding skills
Overview
---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!