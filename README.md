# VG_python_csv
## A wrapped python functions for reading, writing, dumping and loading data from/into (csv) files in the most elegant way.

### Part 1. Load data from file into list (of list)

#### 1. load csv into list of list
data = load_csv(csv_file_path, is_header = False, delimiter=',')

#### 2. only for python 3.
data = load_csv_v2(csv_file_path, is_header = False, delimiter=',')
data = myload_csv(csv_file_path, is_header = False, delimiter=',')

#### 3. require pandas
#import pandas as pd
data = load_csv_as_list_by_pandas(csv_file_path, is_header = False, delimiter=',')

#### 4. load csv into a dataframe in pandas
df = load_csv_as_df_by_pandas(csv_file_path, delimiter=',')


### Part 2. Write the list of list to a csv. 

#### 5. write a list of list to a csv file. 
#### Note: only for 2 dimension list. The header should also be a list, rather than a string. E.g. header =  ['h1','h2','h3']
#### quoting: csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE
writelist_tocsv(output_file, list_of_list, header = None, mode = 'w', quoting=csv.QUOTE_MINIMAL)

#### 6. add list of list to the csv file
addlist_tocsv(output_file, list_of_list, header = None, quoting=csv.QUOTE_MINIMAL)

#### 7. only write one item of list to the csv file
additem_oflist_tocsv(output_file, item_of_list, header = None, quoting=csv.QUOTE_MINIMAL)
additem_tocsv(output_file, item_of_list, header = None, quoting=csv.QUOTE_MINIMAL)
        
#### 8. save list with header to a csv file using pandas. 
#### For 1 or 2 dimension list header should also be a list, rather than a string. E.g. header = header = ['h1','h2','h3']

#import pandas as pd
writelist_tocsv_pd(csv_file, data_list, header = None,quoting=csv.QUOTE_MINIMAL)

#### 9. write multiple lines into a file, for 1-dimension list
#### By default clean the existed content and write new content. In case append to the existed content, use par: mode = 'a'
#### These multiple lines should be formed as a list, i.e. each line as an element in a list. Header is a string.
writelines_tofile(output_file, list_of_lines, header = None, mode = 'w')

#### 10. add one line to a file
addlines_tofile(output_file, list_of_lines, header = None)

#### 11. add lines to a file
addline_tofile(output_file, str_line, header = None)

### Part 3. Serialize data into a file and retrieve it from a file
#### Json files are 10 times larger than pickle files. Therefore, by default, we use pickle
#import pickle
dump_pik(filename, data)
mydump(filename, data)

#### Load the data dumped by pickle
data = load_pik(filename)
data = myload(filename)

#### json based serialisation, readable
#import json
dump_json(filename, data)
data = load_json(filename)


Design with love.
www.Gong.im
