from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from models.userModel import Person

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

# Rota para fazer login
@user_controller.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify', 'WWW-Authenticate': 'Basic realm="Login required!"'}), 401
    
    user = Person.query.filter_by(username=auth.username).first()
    
    if not user:
        return jsonify({'message': 'User not found!'}), 401
    
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    
    return jsonify({'message': 'Password incorrect!'}), 401

# Função para verificar token de autenticação
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(*args, **kwargs)
    
    return decorated
