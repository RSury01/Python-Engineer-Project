# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:18:47 2022

@author: rsuri
"""
#Source: SOURCE : https://www.youtube.com/watch?v=QVrdDJcJQzY
# Import the packages

import xml.etree.ElementTree as ETree
import_pandas as pd
# load and parse the input file
Tree = ETree.parse('D:/INPUT1.XML') # Give input file path
root = Tree.getroot() # xml file parsed done
A = [] # Assign empty list to use later
for ele in root:
    B = {} # Assign empty dictionary to store data values in key:value pair
    for i in list(ele):
        B.update({i.tag: i.text})  # updating dictionary with (tag -> Columns, text -> Rowdata)
        A.append(B) # appending B to list
df = pd.DataFrame(A) # Creating a dataframe..(It is a 2 dimensional data structure)
# consists of 3 components... data, rows and columns
df.drop_duplicates(keep='first', inplace=True) # Delete if any Duplicates
df.reset_index(drop=True, inplace=True) # Reset index after deleting Duplicates
writer = pd.Csvwriter("D:/OUTPUT.csv", engine='csvwriter') #It will create and write data in output file
df.to_csv(writer, sheet_name='sheet1') # Used to export the dataframe to csv file
# if want to add width space to column
worksheet = writer.sheets['sheet1']
worksheet.set_column("B:Z", 30) # Columns from B to Z will increase to 30 characters
writer.save() # It will save the file
print("XML file converted into Csv successfully...")