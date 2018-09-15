# k nearest neighbor algorithm
#imported the  sklearn package for accuracy,metrics,datasets,split train & test data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets
#loaded  iris datasets
dataset =datasets.load_iris()
#loaded the  data & target into x and y
x=dataset.data
y=dataset.target
#spliting the  training & testing data into x and y with 20% testing data & 80%training data
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=25)
#defining  the kmean model to perform the KNN algorithm
kmeanmodel=neighbors.KNeighborsClassifier(n_neighbors=50)
#fitting the  training data into kmeanmodel
kmeanmodel.fit(train_x, train_y)
#predicting kmean for test data
predict=kmeanmodel.predict(test_x)
#calculating  the accuracy score using kmean model
print("Accuracy is: :", accuracy_score(predict, test_y))