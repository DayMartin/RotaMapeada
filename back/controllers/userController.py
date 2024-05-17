from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from db.database import get_mysql_connection
from models.userModel import Person
from werkzeug.security import check_password_hash

user_controller = Blueprint('user_controller', __name__)

person = Person()

# Rota para criar uma nova pessoa
@user_controller.route('/register', methods=['POST'])
def create_person():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        person.create(username, password)
        return jsonify({'message': 'Novo usuário criado!'}), 201
    else:
        return jsonify({'error': 'Nome de usuário e senha são necessários!'}), 400
    

@user_controller.route('/consulta/user', methods=['GET'])
def consultar_users():
    conn = get_mysql_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM people")
    users = cursor.fetchall() 
    cursor.close()
    conn.close()

    if not users:  
        return jsonify({'message': 'Usuários não encontrados!'}), 404 
    return jsonify(users), 200  


@user_controller.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Credenciais não fornecidas!'}), 401

    conn = get_mysql_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM people WHERE username = %s", (auth.username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not user:
        return jsonify({'message': 'Usuário não encontrado!'}), 401

    if not check_password_hash(user['password'], auth.password):
        return jsonify({'message': 'Senha incorreta!'}), 401
    
    return jsonify({'message': 'Login efetuado com sucesso!'}), 200

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.args.get('token')
        
#         if not token:
#             return jsonify({'message': 'Token ausente!'}), 401
        
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#         except:
#             return jsonify({'message': 'Token inválido!'}), 401
        
#         return f(*args, **kwargs)
    
#     return decorated