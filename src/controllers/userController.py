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
            # us= Users.query.all()
            users= Users.query.all()
            return jsonify(users)
        except:
            return jsonify({"msg":"error al buscar usuarios"})
#GET USER BY ID
@userContoller.route('/<id>', methods=['GET'])
def getUser(id):
    try:
        usuario = Users.query.filter_by(id=id).first()
        return jsonify(usuario)
    except:
        return jsonify({"msg":"error al buscar el usuario"})

#POST USER
@userContoller.route('/', methods=["GET","POST"])   
def saveUser():
    with Session(engine) as s:
        if request.method == "POST":
            try:
                
                username = str(request.json['username'])
                password = generate_password_hash(request.json['password'])
                fullname = str(request.json['fullname'])
                print(f"username:{username},password:{password},fullname:{fullname}")
                user=Users(Username=username,Password=password,Fullname=fullname)
                print(user)
                try:
                    s.add(user)
                    s.commit()
                    return jsonify({"msg":"El usuario se creo correctamente"})
                except:
                    return jsonify({"msg":"error al generar el usuario"})
            except:
                return jsonify({"msg":"error al guardar el usuario"})
    
