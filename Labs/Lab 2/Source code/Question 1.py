#e prediction model using  with Linear Discriminant Analysis*.
# imported the sklearn packages to perform the LinearDiscriminantAnalysis,LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
# loaded the data
data=load_iris()
x=data.data
y=data.target
# spliting the data set to testing and training with split ratio
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=15)
# Linear LinearDiscriminantAnalysis and the logstic regression
ldamodel=LinearDiscriminantAnalysis()
logmodel=LogisticRegression()
ldamodel.fit(train_x,train_y)
liprediction=ldamodel.predict(test_x)
print("Linear regression accuracy is-LDA ", accuracy_score(liprediction, test_y))
logmodel.fit(train_x, train_y)
loprediction=logmodel.predict(test_x)
print("Logistic regression accuracy is ", accuracy_score(loprediction, test_y))