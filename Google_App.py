import pandas as pd
#import os
#os.chdir('/Users/saurabhphd81/Desktop/TAD/Python_Learning /Python_Code_Practice')
#print(os.getcwd())

gapp =  pd.read_csv('/Users/saurabhphd81/Desktop/TAD/Python_Learning /Python_Code_Practice/googleplaystore.csv')
gapp.head(10)

gapp.shape
gapp.describe()
#Boxplot
gapp.boxplot()
#Histogram
gapp.hist()

# NUll Values 

gapp.info()

