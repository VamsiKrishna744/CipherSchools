# -*- coding: utf-8 -*-
"""Lecture-18(Introduction to Matplotlib and Seaborn).ipynb

"""

#cration a simple line plot with Matplotlib
#pip install matplotlib
import matplotlib.pyplot as plt

#raw data
x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot
#plt.plot(x, y,linestyle="dotted")
plt.plot(x, y,linestyle="dashed")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot
plt.plot(x, y,ls="-")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot
plt.plot(x, y,ls="--")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot
plt.plot(x, y,ls="--")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot
plt.plot(x, y,ls=" ")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot
plt.plot(x, y,ls="-",color='y')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

#adding line width
x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot
plt.plot(x, y,ls="-",linewidth="10")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a line plot adding
#plt.plot(x, y,ls="-",lw="5",marker="P",mec='r',ms="15")
plt.plot(x, y,ls="-",lw="5",marker="P",mfc='r',ms="15")


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

#using numpys
import numpy as np
y1= np.array([4,5,6,7,8])
y2=np.array([1,2,3,4,5])
plt.plot(y1)
plt.plot(y2)
plt.show()

#scatter plots
x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a Scatter plot
plt.scatter(x, y,ls="-")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')
plt.show()

#scatter plots
x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a Scatter plot
plt.scatter(x, y,ls="-",color='Red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')
plt.show()

#Bar Plots
x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a bar plot
plt.bar(x, y,ls="-")

plt.xlabel('Sales')
plt.ylabel('Product')
plt.title('Simple bar Plot')
plt.show()

#Bar Plots
x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a bar plot
plt.barh(x, y,ls="-")

plt.xlabel('Sales')
plt.ylabel('Product')
plt.title('Simple bar Plot')
plt.show()

#Bar Plots
x = [1,2,3,4,5]
y = [4,2,1,7,8]
#creating a bar plot
plt.bar(x, y,ls="-",color="Red",width=0.7)

plt.xlabel('Sales')
plt.ylabel('Product')
plt.title('Simple bar Plot')
plt.show()

#Creating a Histrogram Graphs
#Histrogram Plots
x = [1,2,3,4,5]
#Histrogram a plot
plt.hist(x, bins=4)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Histrogram  Plot')
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [4, 2, 1, 7, 8]

# creating a bar plot
plt.bar(x, y)

plt.xlabel('Sales')
plt.ylabel('Product')
plt.title('Simple Bar Plot')
plt.show()

#creation of a subplots with matplotlib
#data
x = [1,2,3,4,5]
y = [2,3,4,5,6]
z = [7,8,9,4,5]
#creation of subplots
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[0].set_title('First plots')
axs[1].plot(x, z, color='red')
axs[1].set_title('Second Plot')
#Displaying the plots
plt.tight_layout()
plt.show()

#plots with Annotations
x = [2,3,4,5,6]
y = [7,8,9,4,5]
#creation of Annotations
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plots with Annotations')
plt.annotate('peak', xy=(6, 5), xytext=(4, 9), arrowprops=dict(facecolor='black',shrink=0.05))
#xytext indicates where the arrows starts
plt.show()

#creation of simple line plots with seaborn
import seaborn as sns
import matplotlib.pyplot as plt
x = [2,3,4,5,6]
y = [7,8,9,4,5]

#creation of line plots
sns.scatterplot(x=x, y=y)
plt.xlabel('Laxman')
plt.ylabel('Reddy')
plt.title('Simple line plots with seaboen')
plt.show()

#creation of simple bar plots with seaborn
#data
cat= ['A','B','C','D','E']
values = [4,8,5,4,9]
#cretion of barplots
sns.barplot(x=cat, y=values)
plt.xlabel('Laxman')
plt.ylabel('Reddy')
plt.title('Simple bar plots with seaboen')
plt.show()

#creation of histogram
d=[1,4,5,6,8,9,3]
sns.histplot(d, bins=4)
plt.xlabel('values')
plt.ylabel('frequency')
plt.title('Simple histrogram  `  with seaboen')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = sns.load_dataset("iris")

# creation of the pair plots
sns.pairplot(iris, hue='species')

plt.title('Pair plots with seaborn')
plt.show()

#creation of heatmap
import numpy as np
d= np.random.rand(10, 12)
sns.heatmap(d)
plt.title('Heat with Seaborn')
plt.show()
