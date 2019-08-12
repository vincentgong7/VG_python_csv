# VG_python_csv
A python lib to read and write csv files.

# -----------------------------------------
# Load data from file into list (of list)

# load csv into list of list
data = load_csv(csv_file_path, is_header = False, delimiter=',')

# only for python 3.
data = load_csv_v2(csv_file_path, is_header = False, delimiter=',')
data = myload_csv(csv_file_path, is_header = False, delimiter=',')

# require pandas
# import pandas as pd
data = load_csv_as_list_by_pandas(csv_file_path, is_header = False, delimiter=',')

# load csv into a dataframe in pandas
df = load_csv_as_df_by_pandas(csv_file_path, delimiter=',')

# ----------------------------------------------
# write the list of list to a csv. Note: only for 2 dimension list.
# header should also be a list, rather than a string.
# eg. header = header = ['h1','h2','h3']
# csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE
writelist_tocsv(output_file, list_of_list, header = None, mode = 'w', quoting=csv.QUOTE_MINIMAL)

# add list of list to the csv file
addlist_tocsv(output_file, list_of_list, header = None, quoting=csv.QUOTE_MINIMAL)

# only write one item of list to the csv file
additem_oflist_tocsv(output_file, item_of_list, header = None, quoting=csv.QUOTE_MINIMAL)
additem_tocsv(output_file, item_of_list, header = None, quoting=csv.QUOTE_MINIMAL)
        
# save list with header to a csv file using pandas. For 1 or 2 dimension list
# header should also be a list, rather than a string.
# eg. header = header = ['h1','h2','h3']
# csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE
# import pandas as pd
writelist_tocsv_pd(csv_file, data_list, header = None,quoting=csv.QUOTE_MINIMAL)

# write multiple lines into a file, for 1-dimension list
# by default clean the existed content and write new content
# in case append to the existed content, use par: mode = 'a'
# these multiple lines should be formed as a list, i.e. each line as an element in a list.
# header is a string.
writelines_tofile(output_file, list_of_lines, header = None, mode = 'w')

# add one line to a file
addlines_tofile(output_file, list_of_lines, header = None)

# add lines to a file
addline_tofile(output_file, str_line, header = None)

# Serialize data into a file and retrieve it from a file
# json files are 10 times larger than pickle files
# by default, we use pickle
# import pickle
dump_pik(filename, data)
mydump(filename, data)

# Load the data dumped by pickle
data = load_pik(filename)
data = myload(filename)

# json based serialisation, readable
# import json
dump_json(filename, data)
data = load_json(filename)


Design with love.
www.Gong.im
