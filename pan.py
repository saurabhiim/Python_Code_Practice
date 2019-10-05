import pandas as pd

import os
os.chdir('/Users/saurabhphd81/Desktop/TAD/Python_Learning /Python_Code_Practice')
print(os.getcwd())


a = {
"name": ['saurabh', 'lui','Medha', 'Tridev', 'vasu','shiv'],
"marks": [87,67,93,76,65,81],
"city": ['Mumbai', 'Ahmedabad', 'Dubai', 'New Delhi', 'patna', 'hyderabad']
}

#df = pd.DataFrame(a)

#df.to_csv("friend.csv", index=False)
#print(df)
#df.head(1)
#df.describe()

 

df =  pd.read_csv('Diabetes.csv')
df.shape()

df['glucose_conc'].max()
df['glucose_conc'].mean()
#df.describe()
#df.head()
#df.tail()

# Important Parametes in the pandas 

# We are using the Data Frames

df.shape
#df.head()
import pandas as pd 
import numpy as np
import sklearn as sk

dat = pd.read_csv('data.csv')

# This Will tell the No of Rows and Columen in the CSV File
dat.shape


dat.head()

#Takes data from 0 to n-1 Rows
dat[12:23]

dat.columns
#Specific Column 
dat.x1
dat['x2']

#OR 

dat['y']


#dat[['x1','y'] ]


#ny.array(dat)

X = np.array(dat[['x1', 'x2']])
y = np.array(dat['y'])

print(X)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

classifier = SVC(kernel = 'rbf', gamma = 200)
# Fit the classifier
classifier.fit(X,y)


cl  =  LogisticRegression()


cl.fit(X,y)





