
#Assume you have a SQLAlchemy model Employee with the fields id, 
#name, and salary. Write a SQLAlchemy query to fetch all employees whose salary is greater than 50000.


from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Employee(Base):
	__tablename__ = 'employee'
	id = Column(Integer,primary_key=True)
	name = Column(String(50))
	salary = Column(Float)
	dob = Column(String(50))
	department = Column(String(50))
	email = Column(String(100))
	
	
engine = create_engine('mysql+pymysql://amohmad:welcome@localhost/practise')  # MySQL example


Session = sessionmaker(bind=engine)
session = Session()

result = session.query(Employee).filter(Employee.department=='IT').all()

for employee in result:
	print(employee.id,employee.name,employee.email)