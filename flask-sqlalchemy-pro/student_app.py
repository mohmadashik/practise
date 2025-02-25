from flask import Flask,jsonify
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://amohmad:welcome@localhost:3306/practise'
app.config['TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer,primary_key=True,nullable=False,auto_increment=True,unique=True)
    name = db.Column(db.String(50),default=None)
    age = db.Column(db.Float,nullable=True)

class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer,primary_key=True,nullable=False,auto_increment=True,unique=True)
    name = db.Column(db.String(30),nullable=False)
    chapters= db.Column(db.Integer,nullable = True,default=0)

class Results(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer,primary_key=True,auto_increment=True)
    student_id = db.Column(db.Integer,nullable=False)
    subject_id = db.Column(db.Integer,nullable=False)
    marks = db.Column(db.Float,nullable=True,default=00)

# with app.app_context() as app_context:
#     db.create_all()

@app.route('/tables-create')
def create_tables():
    db.create_all()
    return 'done'

@app.route('/add-students')
def add_students():
    stud1 = Student(name='hema',age=10)
    stud2 = Student(name='venu',age=12)
    stud3 = Student(name='fayaz',age=13)
    stud4 = Student(name='john',age=14)
    db.session.add_all([stud1,stud2,stud3,stud4])
    db.session.commit()
    return 'students added'


@app.route('/add-subjects')
def add_subjects():
    sub1= Subject(name='Physics',chapters=20)
    sub2= Subject(name='Botany',chapters=25)
    sub3= Subject(name='ComputerScience',chapters=18)
    sub4= Subject(name='Chemistry',chapters=15)
    sub5= Subject(name='Zoology',chapters=30)
    db.session.add(sub1)
    db.session.add(sub2)
    db.session.add(sub3)
    db.session.add(sub4)
    db.session.add(sub5)
    db.session.commit()
    return 'subjects added'

@app.route('/add-results')
def add_results():
    from random import randint
    list_of_results = []
    for student_id in range(6,13):
        for subject_id in range(1,5):
            marks = randint(35,100)
            result_obj = Results(student_id=student_id,subject_id=subject_id,marks=marks)
            list_of_results.append(result_obj)
    db.session.add_all(list_of_results)
    db.session.commit()
    return 'results added'
    # result_1 =  Results(student_id =7,subject_id =1,marks=90)
    # result_2 =  Results(student_id =7,subject_id =2,marks=88)
    # result_3 =  Results(student_id =7,subject_id =3,marks=76)
    # result_4 =  Results(student_id =1,subject_id =4,marks=55)
    # result_5 =  Results(student_id =1,subject_id =5,marks=65)
    # db.session.add_all([result_1,result_2,result_3,result_4,result_5])
    # db.session.commit()

    # result_1 =  Results(student_id =2,subject_id =1,marks=90)
    # result_2 =  Results(student_id =2,subject_id =2,marks=78)
    # result_3 =  Results(student_id =2,subject_id =3,marks=96)
    # result_4 =  Results(student_id =2,subject_id =4,marks=65)
    # result_5 =  Results(student_id =2,subject_id =5,marks=85)

    # db.session.add_all([result_1,result_2,result_3,result_4,result_5])
    # db.session.commit()


    # result_1 =  Results(student_id =3,subject_id =1,marks=80)
    # result_2 =  Results(student_id =4,subject_id =2,marks=80)
    # result_3 =  Results(student_id =4,subject_id =3,marks=56)
    # result_4 =  Results(student_id =4,subject_id =4,marks=85)
    # result_5 =  Results(student_id =4,subject_id =5,marks=95)

    # db.session.add_all([result_1,result_2,result_3,result_4,result_5])
    # db.session.commit()

    # result_1 =  Results(student_id =5,subject_id =1,marks=92)
    # result_2 =  Results(student_id =5,subject_id =2,marks=78)
    # result_3 =  Results(student_id =5,subject_id =3,marks=76)
    # result_4 =  Results(student_id =5,subject_id =4,marks=55)
    # result_5 =  Results(student_id =5,subject_id =5,marks=65)

    # db.session.add_all([result_1,result_2,result_3,result_4,result_5])
    # db.session.commit()

    # result_1 =  Results(student_id =6,subject_id =1,marks=89)
    # result_2 =  Results(student_id =6,subject_id =2,marks=98)
    # result_3 =  Results(student_id =6,subject_id =3,marks=86)
    # result_4 =  Results(student_id =6,subject_id =4,marks=95)
    # result_5 =  Results(student_id =6,subject_id =5,marks=85)

    # db.session.add_all([result_1,result_2,result_3,result_4,result_5])
    # db.session.commit()



    # return 'results added'


@app.route('/query')
def student_search():
    from sqlalchemy import and_
    student_obj = Student.query.filter_by(name='ramu').first()
    print(student_obj.name)
    print(student_obj.age)
    
    subjects  = Subject.query.filter(and_(Subject.name!='English',Subject.id!=1)).all()
    for subject in subjects:
        print(f'name : {subject.name}')
        print(f'chapters : {subject.chapters}')
        print(f'type of each record is {type(subject)}')
        # print(obj_to_dict())
    subject = Subject.query.filter_by(name='English').first()
    print(subject.name)
    print(subject.chapters)
    subjects = Subject.query.filter_by(name='Telugu').all() # filter_by is for simpler expressions.
    #cannot use >,<,!= , or_, and_, like etc
    for subject in subjects:
        print(subject.name)
        print(subject.chapters)
    return 'done'

@app.route('/all-students-marks')
def all_student_marks():
    all_results = db.session.query(Student.id.label('student_id'),Student.name.label('student_name'),\
                                   Subject.name.label('subject_name'),Results.marks.label('marks'))\
                                    .join(Student,Results.student_id==Student.id)\
                                    .join(Subject,Results.subject_id==Subject.id).all()
    response = {}
    for result in all_results:
        if result.student_name in response:
            response[result.student_name]['results'].append({result.subject_name :result.marks})
        else:
            response[result.student_name] = {'results':[]}
            response[result.student_name]['results'].append({result.subject_name :result.marks})
    return jsonify(response)

@app.route('/direct_query')
def direct_query():
    name = db.session.execute(text("SELECT s3_bucket from organization")).scalar()
    print(name.split('-')[2])
    return f'name : {name}'

    # return f'name is {name} , split is {name.split()[1]}'

if __name__ =='__main__':
    app.run(debug=True)
