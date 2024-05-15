### Para iniciar este projeto utilize

```sh
docker-compose up
```

### O Projeto iniciará

- Container MySQL
- Container Backend
- Container Front

Existe uma pasta no backend chamada 'Test' para utilizar os arquivos de teste instale
no vscode a extensão 'REST Cliente'


Front


# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js
nvm install 20

npm install -g @angular/cli
ng new frontnd


pip install folium

from flask import Flask, render_template
import json
import folium

app = Flask(__name__)

@app.route('/mapa')
def mapa():
    # Carregar os dados do arquivo positions.json
    with open('positions.json', 'r') as f:
        data = json.load(f)

    # Criar um mapa com a primeira coordenada como ponto inicial
    m = folium.Map(location=[float(data['data'][0]['latitude']), float(data['data'][0]['longitude'])], zoom_start=12)

    # Adicionar marcadores para cada coordenada
    for point in data['data']:
        folium.Marker(location=[float(point['latitude']), float(point['longitude'])]).add_to(m)

    # Criar uma linha poligonal conectando as coordenadas
    polyline = [(float(point['latitude']), float(point['longitude'])) for point in data['data']]
    folium.PolyLine(polyline, color="blue", weight=2.5, opacity=1).add_to(m)

    # Salvar o mapa como um arquivo HTML
    m.save('templates/mapa.html')

    # Renderizar o template HTML
    return render_template('mapa.html')

if __name__ == '__main__':
    app.run(debug=True)


<!DOCTYPE html>
<html>
<head>
    <title>Mapa</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/leaflet.js"></script>
</head>
<body>
    <div id="map" style="width: 100%; height: 100%;"></div>

    <script>
        var map = L.map('map').setView([-18.92406700, -48.28214200], 12);
        
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
        
        L.marker([-18.92406700, -48.28214200]).addTo(map);
        // Adicione marcadores adicionais conforme necessário
        
        var polyline = L.polyline([
            [-18.92406700, -48.28214200],
            // Adicione coordenadas adicionais para a linha poligonal
        ], {color: 'blue'}).addTo(map);
    </script>
</body>
</html>
