from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
username='root'
password='1234'
database='task_management'
path='mysql+mysqldb://{}:{}@localhost/{}'.format(username,password,database)
database=create_engine(path)

Session=sessionmaker(bind=database)
session=Session()