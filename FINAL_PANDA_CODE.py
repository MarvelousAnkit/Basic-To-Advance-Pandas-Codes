import pandas as pd
import numpy as np
#CREATING AND EXPORTING CSV FILES
# we have created the dict which contains employer data
employe_data = {"name" : ["Aman","Ankit","Samrat","Riya"],
"Employe_code":["001","002","003","004"],
"city":["patna","mumbai","delhi","gaya"]}

df = pd.DataFrame(employe_data)
# dataFrame will give us the tabular sheet like structure.
#df.to_csv('data1.csv')
# If you open the csv file then there will be index like 0,1,2,3..
df.to_csv('data1_noindex.csv',index=False)

#NOW SUPPOSE YOU JUST WANT TO SEE TOP 2 COLUMN DATA
print(df.head(2))
print("******************Bottom Top Value ***************************************************")
#NOW SUPPOSE YOU WANT TO SEE BOTTOM TOP 2 VALUE
print(df.tail(2))
#STATISTICS OF THE DATA
print("******************STATISTICS OF THE DATA ***********************************************")
print(df.describe())

#READING EXTERNAL CSV FILE 
print("******************READING EXTERNAl CSV FILE ***********************************************")

read = pd.read_csv('data1.csv')
print(read)
#READING PARTICULAR CELL
print("******************READING PARTICULAR CELL***********************************************")

print(read['name'][0])
print(read['name'])

print("################ EXCEPTION - Here we use column*row")


print("******************CHANGING INDEX VALUE ***********************************************")

#read.index=list("A,B,C,D") # dear you are on reading mode this will not work 
#METHOD1
df.index=list("ABCD")
print(df)
#method2 pREFERRED
df.index = ["sl.1","sl.2","sl.3","sl.4"]
print(df)

#SERIES AND DATAFRAME CONCEPT
#SERIES - is one dimensional array which stores single column or row in data frame
#DATAFRAME - A tabular spreadsheet like structure representing rows each of which contains one or multiple column. EXAMPLE : CSV FILE.

print("******************SERIES***********************************************")
df_series = pd.Series(np.random.rand(5))
print(df_series)
print(type(df_series))
# this will generate 5 random row containing some random data
print("******************DATAFRAME***********************************************")
df_dataframes = pd.DataFrame(np.random.rand(3,5))
print(df_dataframes)
print(type(df_dataframes))
print(df_dataframes.dtypes)
#the dtypes is object because it contains many type of data type like int,string
df_dataframes[1][0]=2
#COLUMNS X ROWS
print(df_dataframes)
print("******************CONVERTING CSV DATA TO NUMPY ARRAY ***********************************************")
#this will convert the code into numpy array
print(df_dataframes.to_numpy())
print("******************CONVERTING CSV DATA TO CSV FORMAT ***********************************************")
print(df_dataframes.to_csv())
print("******************COPING DATA***********************************************")
df_new = df_dataframes
print("NOTE THAT DF_NEW IS JUST POINTING TO df_dataframes. dFNEW IS NOT THE COPY OF df_dataframe. bUT IF YOU CHANGE ANYTHING IN DF_NEW IT WILL BE IMPLEMENTED IN df_dataframes")
df_new[0][1]='59.999'
print(df_new)
print("*******************************************************")
print(df_dataframes)
#FOR COPING DATAFRAMES,SERIES THERE ARE TWO METHOD
#1) .COPY()
df_new1 = df_dataframes.copy()
print("****************METHOD 1********************************8")
print(df_new1)
print("****************METHOD 2********************************8")
df_new2 = df_dataframes[:]
print(df_new2)
print("***************************LOC METHOD TO CHANGE DATA ******************")
#preffered way to cahnge the data
df_new2.loc[0,0]="NULL"
#THIS USES Row X Column 
print("THIS USES ROW X COLUMN")

df_new2.columns = ["A" , "B" , "C" , "D", "E"]
df_new2.loc[0,'B']="null"

print(df_new2)

print("***************************DELETING SERIES FROM THE DATAFRAMES ******************")
#deleting column
df_new2.drop('E',axis=1,inplace=True)

#deleting Index/Row
df_new2.drop(1,axis=0,inplace=True)
#NOTE IF YOU DO THIS THEN DATA WILL BE DELETED FROM THE ORIGINAL DATAFRAME

print("***********************Viewing Specific CSV Part in VSCODE ****************************")
#FORMAT ROW*COLUMN : JAHA COMMA LAGA WO ROW INTO COLUMN FORMAT

print(df_new2.loc[[0],['A']])
print(df.loc[['sl.1'],['name']])
print("Yes this works for All Format")
# YOU WANT SPECIFIC ROW AND ALL COLUMN

print(df_new2 )
print("*******************")
print(df_new2.loc[[2] , :])

print("***************************VIEWING COLUMN LESS THAN x*************************************")
print(df_new)
print(df_new.loc[(df_new[1]>1)])
#This will show value greator than 1 but keep in mind if the column contain any string value than this trick will not work !
#This will show error can compare between int and string.

#I LOC METHOD TO SELECT CELL USING INDEX OF COLUMNS AND ROWS
print("**********************************I LOC Method*************************************************")
print(df_new)
print(df_new.iloc[1,1]) # The value should be 0.10443824964084947
# [Rows index , column index]
# Showing Multiple columns using Iloc
print(df_new.iloc[[0,1],[0,1]]) # THis will show you particular column and rows
# DELETING A ROW
print("*************** Deleting a Row ******************************")
print(df_new.drop([0])) 
print("The Row Has Been Deleted Successfully")
print("*************** Deleting a Column ******************************")
print(df_new.drop([3], axis=1)) 
#Note here give the name of the column
print("The Column Has Been Deleted Successfully")
#Concept of inplace = True
print(df_new.drop([2], axis=1)) 
print(df_new.drop([1], axis=1)) 
print("*******************The column is not deleted from the original dataFrame******************")
print(df)
print(df.drop(['name'],axis=1,inplace=True))
print(df)
print("The Column has been deleted permanently from the dataframe")
#The will modify the original sheet
print("************************* RESETING INDEX*************************")
print(df_new2)
print(df_new2.reset_index())
# This will reset the index and give an extra column named as index . To prevent this use Drop=True

print(df_new2.reset_index(drop=True,inplace=True))
print(df_new2)
print("IF any column value is None it will return True otherwise False ")
print(df_new2['A'].isnull()) 
print("Changing value of column b")
print(df_new2)
df_new2['A'] = None
print(df_new2)
print(df_new2['A'].isnull())
print("ALWAYS USE LOC METHOD TO CHANGE ANY  KIND OF DATADATA")
# sab row ke sab column me
df_new2.loc[:  ,['B']]=None
"""This will only set none in B column of 0 index/ row
df_new2.loc[[0]  ,['B']]=None"""

print(df_new2)


 





















