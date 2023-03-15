from sklearn import datasets
import pandas as pd
import os


iris = pd.DataFrame(datasets.load_iris().data)

iris.to_csv("iris_df.csv")