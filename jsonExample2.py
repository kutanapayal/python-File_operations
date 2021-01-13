import json

input='''[
        {"id":"001",
         "name":"payal",
         "phone":"86732 56678"
        },
        {"id":"002",
         "name":"Riya",
         "phone":"78543 56754"
        }
    
]'''

data=json.loads(input)
print("Number of Users :",len(data))
for item in data:
    print("Id",item["id"])
    print("Name :",item["name"])
    print("Phone",item["phone"])