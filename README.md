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

### A rota para inclusão de pontos atualiza os dados de positions.json

Front

#### Se você já tiver o MYSQL instalado em seu computador, aconselho pausa-lo para não dar conflitos de porta com o container

```sh
sudo systemctl stop mysql
```


# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js
nvm install 20

npm install -g @angular/cli
ng new frontnd



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
