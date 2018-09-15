#Implement Support Vector Machine classification,a. Choose one of the datasetsusing the datasets features in the scikit-learnb. Load the datasetc. According to your dataset, split the data into 20% testing data, 80% training data(youcan also use any other number)d. Apply SVC with Linear kernele. Apply SVC with RBF kernelf. Report the accuracy of the model on both models separately and report their differences if there are anyg. Report your view how can you increase the accuracy and which kernel is the best for your dataset and why
#imported the packages from sklearn module  for support vector , accuracy, split train data and datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
#load the iris datasets
data=datasets.load_iris()
#load x and y data
x=data.data
y=data.target
#spliting the training and test data for both x and y for linear kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=21)
#spliting the training and test data for both x and y for rbf kernel
train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.2, random_state=19)
#defining the model for linear kernel
lmodel=SVC(kernel='linear')
#defining  the model for rbf kernel
rmodel=SVC(kernel='rbf')
#fitting the training data into linear kernel
lmodel.fit(train_x, train_y)
#predicting the test data using linear kernel
prediction=lmodel.predict(test_x)
#calculate the  accuracy score for linear kernel
print("Linear kernel Accuracy score is", accuracy_score(prediction, test_y))
print(prediction)
#fitting the  training data into rbc kernel
rmodel.fit(train_x1, train_y1)
#predicting the test data for rbc kernel
pred=lmodel.predict(test_x1)
#calculated theb  accuracy for rbc kernel
print("RBF kernel accuracy score is", accuracy_score(pred, test_y1))
print(pred)