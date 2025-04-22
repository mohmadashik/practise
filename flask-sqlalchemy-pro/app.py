
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



# # from flask import Flask
# # app = Flask(__name__)
# # db =  app # 

# class Student(db.Model):
#     id = db.Column(db.Integer,primary_key=True,auto_increment=True)
#     name = db.Column(db.VARCHAR(len=250),null=False)
#     class = db.Column(db.VARCHAR(len=100),null=False)
#     rollno = db.Column(db.BIGINTEGER,null = False)
#     school_id = db.Column(db.Integer,null = False)
#     active = db.Column(db.Boolean,null = False,default=1)

# class School(db.Model):
#     id = db.Column(db.Integer,primary_key=True,auto_increment=True)
#     name = db.Column(db.VARCHAR(len=250),null=False)
#     location = db.Column(db.VARCHAR(len=250),null=True)


@app.route('/school/students')
def get_students():
    id = request.params['id']
    # School.query.join
    'select st.name,st.class,st.active , st.id ,sc.name,sc.id 
from student st join school sc 
on st.school_id = sc.id where st.name like "%input_query_name%"'
    db_result = {}
    result = {}
    for school in db_result:
        result['school_name'] = db_result.name
        result['id'] = db_result.id
        result['student'] = []
        cur_data = {}
        for student in db_result['students']:
            cur_data = {'name':student.name,
             'class':student.class,
             'school_name':db_result.name,
             'active':student.active,
             'id':student.id}
        result['student'].append(cur_data)

    return result

'

'
