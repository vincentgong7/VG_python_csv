#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get_ipython().run_line_magic('run', 'myio.py')
from myio import *


# In[ ]:


# testing data

e = [2.5,3,6,7.8,9.0,'adf',True,'asdf"asdf']
data_dimension1 = e
data_dimension2 = [e,e,e,e]
data_dimension3 = [data_dimension2,data_dimension2,data_dimension2,data_dimension2]

output_file = "./test.file"


# In[ ]:


# examples of writing/dumping data into a file


# In[ ]:


# write a list of list to a csv file
header_list = ['h1','h2','h3','h4','h5','h6','h7','h8']
writelist_tocsv(output_file, data_dimension2, header_list)


# In[ ]:


# append a list of list into a csv file
header_list = ['h1','h2','h3','h4','h5','h6','h7','h8']
addlist_tocsv(output_file, data_dimension2, header_list)


# In[ ]:


# append an item of list into a csv file
additem_tocsv(output_file, data_dimension1)


# In[ ]:


# write a list of list to a csv file using pandas
header_list = ['h1','h2','h3','h4','h5','h6','h7','h8']
writelist_tocsv_pd(output_file, data_dimension2, header_list)


# In[ ]:


# write multiple lines into a file
header_str = 'h1,h2,h3,h4,h5,h6,h7,h8'
writelines_tofile(output_file, data_dimension1, header_str)


# In[ ]:


# append multiple lines into a file
addlines_tofile(output_file, data_dimension1)


# In[ ]:


# append one line to a file
str_line = "Hello world!"
addline_tofile(output_file, str_line)


# In[ ]:


# dump (Serialize) an object (data structure) into a file, using pickle
mydump(output_file, data_dimension3) # same as dump_pik(output_file, data_dimension3)


# In[ ]:


# dump (Serialize) an object (data structure) into a json file, using json
dump_json(output_file, data_dimension3)


# In[ ]:





# In[ ]:


# examples of read/loading data into a file
input_file = "./test.file"


# In[ ]:


# read a csv file into a list of list
data = myload_csv(input_file, is_header = True) # same as: load_csv, load_csv_v2


# In[ ]:


# load a csv file into a list (of list) using pandas
data = load_csv_as_list_by_pandas(input_file)


# In[ ]:


# load a csv file into pandas dataframe
df = load_csv_as_df_by_pandas(input_file)


# In[ ]:


# load (unserialize) an object (data structure) from a file, using pickle
mydata = myload(output_file) # same as load_pik(output_file)


# In[ ]:


# load (unserialize) an object (data structure) from a json file, using json
load_json(output_file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




