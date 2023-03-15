from sklearn import svm
import pandas as pd

df = pd.read_csv("iris_df.csv")

clf = svm.LinearSVC()

clf.fit(iris.data, iris.target)

print("coefficients are:")
print(clf.coef_ )