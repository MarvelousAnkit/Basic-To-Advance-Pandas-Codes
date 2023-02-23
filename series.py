import pandas as pd 
import numpy as np
ser = pd.Series(np.random.rand(3),index=np.arange(3))
df = pd.DataFrame(np.random.rand(18,5) )
# iwant to give 5 rows and 5 column

print((ser))
print(type(df))

data = df.describe()
print(data)
print(df.dtypes)
#the dtypes is object because it contains many type of data type like int,float
df[0]="ankit"
print(df)
df[0]=0
print(df.dtypes)
#
df.head()
print(df.to_numpy())
# this is numpy array
print(df.to_csv())

#df.t will do the transpose

print(df)
print(df[0])
# this is a series
# series ke combination se dataframe banta hai