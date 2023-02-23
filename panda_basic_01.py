import pandas as pd
import numpy as nm

student_data = {"name" : ["ankit","samrat","riya","kunal"],
"marks" : [99,23,34,21],
"city":["patna","patna","patna","patna"]}

df = pd.DataFrame(student_data)
# What is Data Frame ? This is like Excel sheet. This will convert the data into excel sheet format so that we can use numpy function. It will also make the indexing faster


# 0,1,2,3 are the indexes of particular rows , this can be change also ! and name marks city are the columns

#   df.to_csv('filename_with_index.csv') # this will convert the data into csv format

#make  sure to write .csv after file name to convert into csv format

#   df.to_csv('data_no_index.csv' , index=False) # this will remove the index from the excel sheet

top_row=df.head(2) # This will display 2 rows from the top
print(top_row)
last_row = df.tail(2) # this will display the last 2 row
print(last_row)
analize = df.describe() # this will give you all the data like mean mode median etc
print(analize)

"""fd = pd.DataFrame('sample.xlsx')
print(fd.read_csv('sample.xlsx'))""" # This trick will not work to read a file

read = pd.read_csv('book1.csv')
print(read)

read0=read["Name"][0] # this will print the zero index value of Name column
print(read0)

change0=read["Name"][0] = "priyanshu"
print(read)

newfile= read.to_csv("changed_excel_with no index.csv",index=False)

#changing The Index Value

read.index = ['first' , 'second' , 'third' , 'fourth' , 'fifth'] # this will change the index value
print(read)

# to access row there is index to access column there is column name

newfile1 = read.to_csv("book1.csv")

read.index=['name1','name2','name3','name4','name5']
print(read)
