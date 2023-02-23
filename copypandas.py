import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10,5))
#print(df)
df_new = df
#df_new is not coping the df it just pointing the df. whatever changes you will do in df_new will be implemented in df.

df_new[1][3]=48
# if you do like this then 1 is the column and 3 is the row
#print(df) 

new_df3=df[:] #making copy
newdf4=df.copy()
#new_df3[0][0]="Ankit"
##print(new_df3) row*column
#print(df)
# if you make a copy then there will no change in the original file.
#print(newdf4)
df.loc[0][0] = 29999
# the right way to change the value
#print(df)
#changing column
df.columns = list("ABCDE")
# print(df)
df.index=list("0123456789")
# print(df)
df.loc[0,'A'] = "Ankit"
# print(df)
df_new.columns=list("ABCDE")
#print(df_new)
# df_new.loc[1,'A']=238
df_new.head(2)
