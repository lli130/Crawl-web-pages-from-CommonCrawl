# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:29:31 2017

@author: SAM
"""

files_names = 'D:/lly/UN-search engine/Science_Technology_Search-ICT4SD_tools/Science_Technology_Search-ICT4SD_tools/prefix-https%3A--ocw.mit.edu-courses-0'

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:59:46 2017

@author: Liyi Li
"""
import numpy
import pandas as pd
import json
import glob

def process_file (file_path):    #This function handles each file. It creates a Panda data frame of every row.
    allDataFrames = []
    with open(file_path) as f:
        for line in f:
            lineDataFrame = pd.DataFrame(json.loads(line) , index=[0])
            allDataFrames.append(lineDataFrame)
    result = pd.concat(allDataFrames)
    return result

#read all the URL-FETCH files at one time
files_names = 'D:/lly/UN-search engine/Science_Technology_Search-ICT4SD_tools/Science_Technology_Search-ICT4SD_tools/prefix-https%3A--ocw.mit.edu-courses-0'

print files_names
#create Panda dataframe for each file
name_pd = process_file(files_names)
name_pd_output = files_names +'try2.txt'
print str(name_pd.url)
with open(name_pd_output,'a') as f2:
    f2.write(str(name_pd.url))
f2.close()
    
    
#Example, working with the downloaded files using Pandas.
#Afghanistan_File_0 = process_file('./results/' , 'domain-gov.af-0')
#print (Afghanistan_File_0.dtypes)   #Shows the columns
#print (Afghanistan_File_0.head(1))  #Shows the first row of the pandas dataframe
#print (Afghanistan_File_0.url)      #Shows just the column of your interest e.g. url