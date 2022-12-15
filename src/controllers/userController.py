from flask import Blueprint, jsonify, request
from src.models.models import Users, engine
from werkzeug.security import generate_password_hash,check_password_hash

from sqlalchemy.orm import Session
from sqlalchemy import select


userContoller = Blueprint('user',__name__,url_prefix='/user')

#GET ALL USERS
@userContoller.route('/all', methods=['GET'])
def getUsers():
    with Session(engine) as session:
        try:
            stmt = select(Users)
            users = session.scalars(stmt)
            userslist = [user.serialize() for user in users]
            return jsonify(userslist)
        except:
            return jsonify({'result':"error al buscar usuarios"})


#GET USER BY ID
@userContoller.route('/<id>', methods=['GET'])
def getUser(id):
    with Session(engine) as session:
        try:
            user= session.get(Users,id)
            usuario = user.serialize()
            return jsonify(usuario)
        except:
            return jsonify({'result':"error al buscar el usuario"})
#POST USER
@userContoller.route('/', methods=["GET","POST"])   
def saveUser():
    with Session(engine) as s:
        if request.method == "POST":
            try:
                username = str(request.json['username'])
                password = generate_password_hash(request.json['password'])
                fullname = str(request.json['fullname'])
                user=Users(Username=username,Password=password,Fullname=fullname)
                try:
                    s.add(user)
                    s.commit()
                    return jsonify({'result': 'Ok'}), 200
                except:
                    return jsonify({'result':"error al generar el usuario"}), 400
            except:
                return jsonify({'result':"error al guardar el usuario"}), 400

@userContoller.route('/<id>', methods=["DELETE"])
def deleteUser(id):
    with Session(engine) as session:
        try:
            user= session.get(Users,id)
            session.delete(user)
            session.commit()
            return jsonify({'result': 'Ok'}), 200
        except:
                return jsonify({'result':"no se pudo borrar usuario"}), 400
            

@userContoller.route('/<id>', methods=["PUT"])
def updateUser(id):
    with Session(engine) as session:
        try:
            user= session.get(Users,id)
            username = str(request.json['username'])
            password = generate_password_hash(request.json['password'])
            fullname = str(request.json['fullname'])
            user.Username = username
            user.Fullname = fullname
            user.Password = password
            session.commit()
            
            
            return jsonify({'result': 'Ok'}), 200
        except:
                return jsonify({'result':"no se pudo modificar usuario"}), 400
        
#Login de usuario
@userContoller.route('/login', methods=["GET","POST"])
def login():
    with Session(engine) as session:
            data = request.json
            username= data['username']
            password= data['password']
            usuario= select(Users).where(Users.Username == username)
            # usuario = session.query(Users.Username).filter(Users.Username == username)
            esto = session.scalars(usuario)
            return jsonify({'result': 'Ok'})
    