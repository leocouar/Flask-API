from dataclasses import dataclass
from sqlalchemy import DATETIME, Boolean, Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

base = declarative_base()

SQLALCHEMY_DATABASE_URI = 'sqlite:///tfinal.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, future=True)

@dataclass
class Users(base):
    __tablename__= "Users"
    
    Id = int
    Username = str
    Fullname = str
    Password = str
    isAdmin = bool
    
    Id = Column(Integer, primary_key=True, unique=True)
    Username = Column(String(50), nullable=False)
    Fullname = Column(String(50), nullable=False)
    Password = Column(String(250), nullable=False)
    isAdmin = Column(Boolean,default=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
base.metadata.create_all(engine)