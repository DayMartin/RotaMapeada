import json
from flask import Blueprint, jsonify, request
from datetime import datetime, timezone
from flask import Flask, render_template
import json
import folium
# from models.positionModel import Pontos

pontos_controller = Blueprint('pontos_controller', __name__)

# pontos = Pontos()

# Rota para criar novos pontos
@pontos_controller.route('/register/pontos', methods=['POST'])
def create_pontos():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00')

        new_point = {
            "date_time": current_time,
            "latitude": latitude,
            "longitude": longitude
        }

        try:
            with open('back/positions.json', 'r') as file:
                positions_data = json.load(file)
        except FileNotFoundError:
            positions_data = {"data": []}

        positions_data["data"].append(new_point)

        with open('back/positions.json', 'w') as file:
            json.dump(positions_data, file, indent=4)

        return jsonify({'message': 'Novo ponto criado!'}), 201
    else:
        return jsonify({'error': 'latitude e longitude são necessários!'}), 400

@pontos_controller.route('/get/pontos', methods=['GET'])
def get_pontos():
    try:
        with open('back/positions.json', 'r') as file:
            positions_data = json.load(file)
            return jsonify(positions_data), 200
    except FileNotFoundError:
        return jsonify({'error': 'Arquivo de dados não encontrado'}), 404
    

@pontos_controller.route('/mapa', methods=['POST'])
def mapa():

    with open('back/positions.json', 'r') as f:
        data = json.load(f)

    m = folium.Map(location=[float(data['data'][0]['latitude']), float(data['data'][0]['longitude'])], zoom_start=12)

    for point in data['data']:
        folium.Marker(location=[float(point['latitude']), float(point['longitude'])]).add_to(m)

    polyline = [(float(point['latitude']), float(point['longitude'])) for point in data['data']]
    folium.PolyLine(polyline, color="blue", weight=2.5, opacity=1).add_to(m)

    map_file_path = 'mapa.html'
    m.save(map_file_path)

    return render_template('mapa.html')