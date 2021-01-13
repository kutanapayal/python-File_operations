import json

data={}
data['emp_salary']=[]
data['emp_salary'].append({
    'name':"payal",
    'salary':'20000'
})

with open('data1.txt','w')as f:
    json.dump(data,f)