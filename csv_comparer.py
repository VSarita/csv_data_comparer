import csv
import os
import urllib
from pymongo import MongoClient


MONGO_URL = ""

instance = MongoClient(MONGO_URL)

db = instance['']  ##db name

def database_collection(collection_name):
    return db[collection_name]


def get_db_data(collection_name,query):
    return database_collection(collection_name).find(query)

#-----------------------------------------------------------------------------------------------------

file_add= ""
file_name = ""  
db_field=""
search_key = ""

#-----------------------------------------------------------------------------------------------------

def generate_csv(flag, data):


    with open(file_add+flag+"_result"+'.csv', 'w') as csvFile:
        fields = data[0].keys()
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


#-----------------------------------------------------------------------------------------------------

reader = csv.DictReader(open(file_add+file_name+".csv"))

#-----------------------------------------------------------------------------------------------------

print type(reader)
data_list = []
count=1

#-----------------------------------------------------------------------------------------------------

for row in reader:
    print "row count: ",count
    print row
    search_key_element = row.get(search_key,"")
    print search_key_element
    check_point =get_db_data("collection_name",{"db_field":db_field_value,
                                                                   "search_key_element":search_key_element})


    check_point_two = list(check_point)
    print "** ", check_point_two, " **"



    if len(check_point_two)>0:
        row["searched_row_available_or_not"]="Yes"
        data_list.append(row)

    else :
        row["searched_row_available_or_not"] = "No"
        data_list.append(row)

    count+=1

#-----------------------------------------------------------------------------------------------------

print data_list[0].keys()
generate_csv(file_name, data=data_list)

#-----------------------------------------------------------------------------------------------------