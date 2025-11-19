import pandas as pd
from sklearn import tree

dataurl="https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv" 

# Load data
irisdf = pd.read_csv(dataurl)
print(irisdf.head(3))

# Features & target
X = irisdf[['sepal_length','sepal_width','petal_length','petal_width']]
y = irisdf['species']

# Train model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

#kn
#from sklearn.neighbors import kNeighborsClassifier
#clf=kNeighborsClassifier()

# Predict
print(clf.predict([[1, 3, 4, 5]]))
print(clf.score(X, y))
