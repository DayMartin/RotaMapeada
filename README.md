### Este projeto se inicia por partes

### Iniciar o Backend e o Banco de dados

```sh
docker-compose up
```

### Iniciar o Front de dados:
1. No terminal entre na pasta ./frontend
2. No terminal  digite: yarn dev

### O Projeto iniciará

- Container MySQL
- Container Backend
- Server Front ( sem container )

OBS: 

Existe uma pasta no backend chamada 'Test' para utilizar os arquivos de teste instale
no vscode a extensão 'REST Cliente'

### A rota para inclusão de pontos atualiza os dados de positions.json

#### Se você já tiver o MYSQL instalado em seu computador, aconselho pausa-lo para não dar conflitos de porta com o container

```sh
sudo systemctl stop mysql
```

<!-- # installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js
nvm install 20

npm install -g @angular/cli
ng new frontnd -->
