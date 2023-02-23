import pandas as pd
import numpy as np 

df = pd.DataFrame(np.random.rand(3,4))
df.drop(0,axis=0 , inplace=True)
# for row use axis = 0
# for column use axis = 1
df.loc[1,0]='Ankit' #this is more preferred way to edit
#df[1][1] ='Ankit2'
print(df)