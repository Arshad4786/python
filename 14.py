# CSV Read write

import csv

data =[
    ['Name' , 'Score'],
    ['person1', 100],
    ['person2', 100]
]

with open('data.csv','w', newline='') as file:
    writer  = csv.writer(file)
    writer.writerows(data)

print("csv created")

with open("data.csv",'r') as file :
    reader = csv.reader(file)
    for x in reader:
        print(x)
######################################################

# JSON READ WRITE
import json 

json_data = {
    'name' : 'person1',
    'Roll' : 'person2'
}

with open("jsondata.json",'w') as file: 
    json.dump(json_data,file)

print("Json file created succesfully!")

with open('jsondata.json', 'r') as file: 
    x = json.load(file)
    print(x)

#####################################################
# IMPORTING A PACAGE

import math_operation

print(math_operation.add(1,2), math_operation.minus(1,2),math_operation.product(1,2),math_operation.divide(1,2))



