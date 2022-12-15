from dataclasses import dataclass
from sqlalchemy import DATETIME, Boolean, Column, BLOB
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy import Integer, NUMERIC
from sqlalchemy import NVARCHAR
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship,backref
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
    
    
    def __repr__(self) -> str:
        return f"User(Id={self.Id!r}, Username={self.Username!r}, Fullname={self.Fullname!r}, Password={self.Password!r}, isAdmin={self.isAdmin!r})"
    
    def serialize(self):
        return {
            "id": f"{self.Id}",
            "username": f"{self.Username}",
            "fullname": f"{self.Fullname}",
            "isAdmin": f"{self.isAdmin}"
        }  

@dataclass
class Album(base):
    __tablename__= "Album"
    
    AlbumId = int
    Title = str
    ArtistId = int
    Column1 = BLOB
    
    AlbumId = Column(Integer, primary_key=True, unique=True)
    Title = Column(String(50), nullable=False)
    Column1 = Column(BLOB)
    ArtistId = Column(Integer,ForeignKey('Artist.ArtistId'),nullable=False)
    Artist = relationship('Artist')
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialize(self):
        return {
            "AlbumId": f"{self.AlbumId}",
            "title": f"{self.Title}",
            "ArtistId": f"{self.ArtistId}",
        }

@dataclass
class Artist(base):
    __tablename__= "Artist"
    
    ArtistId = int
    Name = NVARCHAR
    
    ArtistId = Column(Integer, primary_key=True,nullable=False)
    Name = Column(NVARCHAR(120))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialize(self):
        return {
            "ArtistId": f"{self.ArtistId}",
            "name": f"{self.Name}",
        }

@dataclass
class Customer(base):
    __tablename__= "Customer"
    
    CustomerId = int
    FirstName = NVARCHAR
    LastName = NVARCHAR
    Company = NVARCHAR
    Address = NVARCHAR
    City = NVARCHAR
    State = NVARCHAR
    Country = NVARCHAR
    PostalCode = NVARCHAR
    Phone = NVARCHAR
    Fax = NVARCHAR
    Email = NVARCHAR
    Support = int
    
    CustomerId = Column(Integer, primary_key=True, unique=True,nullable=False)
    FirstName = Column(NVARCHAR(40),nullable=False)
    LastName = Column(NVARCHAR(20),nullable=False)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60),nullable=False)
    SupportRepId = Column(Integer)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialize(self):
        return {
            "CustomerId": f"{self.CustomerId}",
            "FirstName": f"{self.FirstName}",
            "LastName": f"{self.LastName}",
            "Company": f"{self.Company}",
            "Address": f"{self.Address}",
            "City": f"{self.City}",
            "State": f"{self.State}",
            "Country": f"{self.Country}",
            "PostalCode": f"{self.PostalCode}",
            "Phone": f"{self.Phone}",
            "Fax": f"{self.Fax}",
            "Email": f"{self.Email}",
            
        }
        
@dataclass
class Employee(base):
    __tablename__= "Employer"
    
    EmployerId = int
    FirstName = NVARCHAR
    LastName = NVARCHAR
    BirthDate = DATETIME
    HireDate = DATETIME
    Company = NVARCHAR
    Address = NVARCHAR
    City = NVARCHAR
    State = NVARCHAR
    Country = NVARCHAR
    PostalCode = NVARCHAR
    Phone = NVARCHAR
    Fax = NVARCHAR
    Email = NVARCHAR
    Title = NVARCHAR
    
    EmployerId = Column(Integer, primary_key=True, unique=True,nullable=False)
    FirstName = Column(NVARCHAR(20),nullable=False)
    LastName = Column(NVARCHAR(20),nullable=False)
    BirthDate = Column(DATETIME)
    HireDate = Column(DATETIME)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60))
    Title = Column(NVARCHAR(30))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialize(self):
        return {
            "EmployerId": f"{self.EmployerId}",
            "FirstName": f"{self.FirstName}",
            "LastName": f"{self.LastName}",
            "BirthDate": f"{self.BirthDate}",
            "HireDate": f"{self.HireDate}",
            "Company": f"{self.Company}",
            "Address": f"{self.Address}",
            "City": f"{self.City}",
            "State": f"{self.State}",
            "Country": f"{self.Country}",
            "PostalCode": f"{self.PostalCode}",
            "Phone": f"{self.Phone}",
            "Fax": f"{self.Fax}",
            "Email": f"{self.Email}",
            
        }
        
@dataclass
class Genre(base):
    __tablename__= "Genre"
    
    GenreId = int
    Name = NVARCHAR
    
    GenreId = Column(Integer, primary_key=True,nullable=False)
    Name = Column(NVARCHAR(120))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialize(self):
        return {
            "GenreId": f"{self.GenreId}",
            "name": f"{self.Name}",
        }


@dataclass
class MediaType(base):
    __tablename__= "MediaType"
    
    MediaTypeId = int
    Name = NVARCHAR
    
    MediaTypeId = Column(Integer, primary_key=True,nullable=False)
    Name = Column(NVARCHAR(120))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialize(self):
        return {
            "MediaTypeId": f"{self.MediaTypeId}",
            "name": f"{self.Name}",
        }
    
@dataclass
class Playlist(base):
    __tablename__= "Playlist"
    
    PlaylistId = int
    Name = NVARCHAR
    
    PlaylistId = Column(Integer, primary_key=True,nullable=False)
    Name = Column(NVARCHAR(120))
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialize(self):
        return {
            "PlaylistId": f"{self.PlaylistId}",
            "name": f"{self.Name}",
        }
        
@dataclass
class Track(base):
    __tablename__= "Track"
    
    TrackId = int
    Name = NVARCHAR
    AlbumId = int
    MediaTypeId = int
    GenreId = int
    Composer = NVARCHAR
    Millisecons = int
    Bytes = int
    UnitPrice = NUMERIC
    
    TrackId = Column(Integer, primary_key=True,nullable=False)
    Name = Column(NVARCHAR(200))
    ArtistId = Column(Integer,ForeignKey('Artist.ArtistId'))
    Artist = relationship('Artist')
    MediaTypeId = Column(Integer,ForeignKey('MediaType.MediaTypeId'))
    MediaType = relationship('MediaType')
    GenreId = Column(Integer,ForeignKey('Genre.GenreId'))
    Genre = relationship('Genre')
    Composer = Column(NVARCHAR(220))
    Millisecons = int
    Bytes = int
    UnitPrice = NUMERIC
    
    
    
base.metadata.create_all(engine)