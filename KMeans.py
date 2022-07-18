import pandas as pd
from sklearn.cluster import KMeans as km
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler as mms

df = pd.read_csv('income.csv')

fig=plt.figure(figsize=(20,14))

fig.add_subplot(2,2,1)
plt.scatter(df['Age'],df['Income($)'])
plt.title('Income distribution')
plt.xlabel('Age')
plt.ylabel('Income')

#Scale the dataset to avoid bias as a result of large units.
df['Age']=mms().fit_transform(df[['Age']])
df['Income($)']=mms().fit_transform(df[['Income($)']])
fig.add_subplot(2,2,2)
plt.scatter(df['Age'],df['Income($)'])
plt.title('Scaled data distribution')
plt.xlabel('Scaled_Age')
plt.ylabel('Scaled_Income($)')

#Create an elbow plot to determine the optimum value of K.
Mean_Square_Error=[]
for k in range(1,11):
    x=km(n_clusters=k)
    x.fit(df[['Age','Income($)']])
    Mean_Square_Error.append(x.inertia_)
k_range=range(1,11)
fig.add_subplot(2,2,3)
plt.xlabel('k')
plt.ylabel('Sum of Mean Square Error')
plt.plot(k_range,Mean_Square_Error)
plt.title('Elbow plot')

#Predict the clusters and visualize the result using scatter plots.
df['Cluster']=km(n_clusters=3).fit_predict(df[['Age','Income($)']])
df1=df[df.Cluster==0]
df2=df[df.Cluster==1]
df3=df[df.Cluster==2]
fig.add_subplot(2,2,4)
plt.scatter(df1['Age'],df1['Income($)'],color='red')
plt.scatter(df2['Age'],df2['Income($)'],color='green')
plt.scatter(df3['Age'],df3['Income($)'],color='blue')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title('Visualization of clusters')