#Python progrsm to read json file
import json

#Opening JSON file
jsonfile=open('files/data.json')

#returns JSON object as a dictionary
data=json.load(jsonfile)

#Iterating through the json list
for i in data['emp_details']:
    print(i)

#Closing file
jsonfile.close()