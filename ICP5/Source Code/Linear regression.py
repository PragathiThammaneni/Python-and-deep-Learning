import numpy as np # imported the numpy library
import matplotlib.pyplot as plt  # imported the matplotlib libraray
x=np.array([0,1,2,3,4,5,6,7,8,9])  # logic for plotting the regerssion model using numpy .
y=np.array([1,3,2,5,7,8,8,9,10,12])
meanx=np.mean(x)
meany=np.mean(y)
num=np.sum((x-meanx)*(y-meany))
den=np.sum(pow((x-meanx),2))
slope=num/den # finding the slope
intercept=meany-(slope*meanx) # finding the intercept
print("slope",slope) # printing the slope
print("intercept",intercept) # printing the intercept
val=(slope*x)+intercept # y=mx+c
plt.plot(x,y) # plotting the graph
plt.plot(x,val)
plt.show()