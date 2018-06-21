# importing the required packages pandas ,sklearn ,matplotlib and numpy
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
# read the data from pandas
data = pd.read_csv("sample_stocks.csv")
X = data.iloc[:,0]
y = data.iloc[:,1]
# Make a 2D array to give input to kmeans
X = np.vstack((X,y)).T
sete={}
for k in range(1,11):
    # use the KMeansclustering
    kmeans = KMeans(n_clusters=k)
    # fit the model to the array X
    kmeans.fit(X)
    # Scatter plot the datapoints with different colors assigned to various clusters
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
    # Scatter plot the centroids with black color
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
    # show the plot using matplotlib package
    plt.show()
    # calculate the sum of squares for every cluster using the kmeans.inertia_
    sete[k] = kmeans.inertia_  #

# plot to choose the best k by using sum of squares b/w each member of cluster and its centroid.
print(sete)
# plot the sse and k values using matplotlib
#plt.plot(sete.keys(), sete.values())
#show the plot
#plt.show()
