###### JSON Example with a Dictionary

import json

data = ''' {
"Name": "Chuck", "Phone": {"type":"intl", "number": "25498866"
},"email":{"hide": "yes"}
}'''

info = json.loads(data)
print("Name:", info["Name"])
print("hide:", info["email"]["hide"])
print("Phone:", info["Phone"]["type"])


###### JSON Example with a List

data1 = '''[ {"name":"ram",
"phone": "548743",
"value":"NONE"
}, {"name": "jad", "phone": "62468746", "value":"MAN"}
]
'''
info1 = json.loads(data1)

print("User Count:", len(info1))
for word in info1:
    print("Name:",word["name"])
