# import requests
import json
import csv
import sys
# import os
import numpy as np
import pickle
from random import randint
import pandas as pd

# ----------------------------------------------------------------------------
# load csv into list of list
def load_csv(csv_file_path, is_header = False, delimiter=','):
    records = []
    with open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        if is_header:
            next(csv_reader, None)
        for row in csv_reader:
            records.append(row)
    print('Read csv file: {} records in {}.'.format(len(records), csv_file_path))
    return records

# only for python 3.
def load_csv_v2(csv_file_path, is_header = False, delimiter=','):
    records = []
    with open(csv_file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        if is_header:
            next(csv_reader, None)
        records = list(csv_reader)
    print('Read csv file: {} records in {}.'.format(len(records), csv_file_path))
    return records

def myload_csv(csv_file_path, is_header = False, delimiter=','):
    return load_csv_v2(csv_file_path, is_header = is_header, delimiter=delimiter)

# require pandas
# import pandas as pd
def load_csv_as_list_by_pandas(csv_file_path, is_header = False, delimiter=','):
    df = pd.read_csv(csv_file_path, delimiter=delimiter)
    if(is_header):
        result = df.values.tolist()
    else:
        result = [df.columns.values.tolist()] + df.values.tolist()
    return result

# require pandas
# load csv into a dataframe in pandas
# import pandas as pd
def load_csv_as_df_by_pandas(csv_file_path, delimiter=','):
    return pd.read_csv(csv_file_path, delimiter=delimiter)

# ----------------------------------------------------------------------------
# write the list of list to a csv. Note: only for 2 dimension list.
# header should also be a list, rather than a string.
# eg. header = header = ['h1','h2','h3']
# csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE
def writelist_tocsv(output_file, list_of_list, header = None, mode = 'w', quoting=csv.QUOTE_MINIMAL):
    with open(output_file, mode = mode, newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',', quoting=quoting)
        if(header != None):
            writer.writerow(header)
        writer.writerows(list_of_list)

# add list of list to the csv file
def addlist_tocsv(output_file, list_of_list, header = None, quoting=csv.QUOTE_MINIMAL):
    writelist_tocsv(output_file, list_of_list, header = header, mode = 'a', quoting=quoting)

# only write one item of list to the csv file
def additem_oflist_tocsv(output_file, item_of_list, header = None, quoting=csv.QUOTE_MINIMAL):
    list_of_list = [item_of_list]
    writelist_tocsv(output_file, list_of_list, header = header, mode = 'a', quoting=quoting)

def additem_tocsv(output_file, item_of_list, header = None, quoting=csv.QUOTE_MINIMAL):
    additem_oflist_tocsv(output_file, item_of_list, header = header, quoting=quoting)
        
# save list with header to a csv file using pandas. For 1 or 2 dimension list
# header should also be a list, rather than a string.
# eg. header = header = ['h1','h2','h3']
# csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE
# import pandas as pd
def writelist_tocsv_pd(csv_file, data_list, header = None,quoting=csv.QUOTE_MINIMAL):
    df = pd.DataFrame(data_list, columns=header)
    df.to_csv(csv_file, index=False, quoting=quoting)

# write multiple lines into a file, for 1-dimension list
# by default clean the existed content and write new content
# in case append to the existed content, use par: mode = 'a'
# these multiple lines should be formed as a list, i.e. each line as an element in a list.
# header is a string.
def writelines_tofile(output_file, list_of_lines, header = None, mode = 'w'):
    myfile = open(output_file, mode = mode, newline="", encoding="utf-8")
    if(header != None):
        myfile.write("{}\n".format(header))
    for line in list_of_lines:
        myfile.write("{}\n".format(line))
    myfile.close()

# add one line to a file
def addlines_tofile(output_file, list_of_lines, header = None):
    writelines_tofile(output_file, list_of_lines, header = header, mode = 'a')

# add lines to a file
def addline_tofile(output_file, str_line, header = None):
    list_of_lines = [str_line]
    addlines_tofile(output_file, list_of_lines, header = header)

# Serialize data into a file and retrieve it from a file
# json files are 10 times larger than pickle files
# by default, we use pickle
# import pickle
def dump_pik(filename, data):
    pickle.dump(data,open(filename, 'wb'))

def load_pik(filename):
    return pickle.load(open(filename, "rb"))

def mydump(filename, data):
    dump_pik(filename, data)

def myload(filename):
    return load_pik(filename)

# json based serialisation, readable
# import json
def dump_json(filename, data):
    json.dump(data,open(filename, 'w', encoding="utf-8"))

def load_json(filename):
    return json.load(open(filename, 'r', encoding="utf-8"))

print("hello world!")
