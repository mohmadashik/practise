a = [2,3,10,1,9,7,4,8,0]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)

'''

model school

name (string), id, location(string)

students

name(string), class(stinr), roll no (big int), school_id(foreign key), active (boolean)
[
    {
        "school_name": "name",
        "id": "",
		{
        "students": [
            {
                "name": "",
                "class": "",
                "active": "",
				 "school_name": "name",
				"id": ""
            },
            {
                "name": "",
                "class": "",
                "active": "",
				"school_name": "name",
				"id": ""
            }
        ]
		}
    }
]
'''