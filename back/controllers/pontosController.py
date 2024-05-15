from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from models.positionModel import Pontos
from db.database import get_mysql_connection

pontos_controller = Blueprint('pontos_controller', __name__)

pontos = Pontos()

# Rota para criar novos pontos
@pontos_controller.route('/register/pontos', methods=['POST'])
def create_pontos():
    data = request.get_json()
    date_time = data.get('date_time')
    latitude = data.get('latitude')
    longitude = data.get('longitude')


    if latitude and longitude:
        pontos.create(latitude, longitude)
        return jsonify({'message': 'Novo ponto criado!'}), 201
    else:
        return jsonify({'error': 'latitude e longitude são necessários!'}), 400
