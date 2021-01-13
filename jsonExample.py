import json
data='''{
        "name" : "payal",
        "phone":{
            "type":"intl",
            "no":"+1 23 456 789"
         },
         "email":{
            "hide":"yes"
          }
        }'''
info=json.loads(data)
print("Name :",info["name"])
print("Phone:",info["phone"]["no"])