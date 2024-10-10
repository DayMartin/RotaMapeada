
![image](https://github.com/user-attachments/assets/61ebd563-a636-465b-923b-737ed95b827a)
![image](https://github.com/user-attachments/assets/663dc4c8-c67a-47fe-a69b-5be6d9de398a)
![image](https://github.com/user-attachments/assets/e447b5d0-0ac9-4465-9efd-b38c36a546a9)
![image](https://github.com/user-attachments/assets/972bf736-4ab5-4f2b-a7f6-4ba01a9efcda)


### Como usar este projeto

### Iniciar o Backend e o Banco de dados

1. No terminal entre no diretório ./back
2. Digite o comando abaixo:

```sh
docker-compose up
```

### Iniciar o Front:
1. No terminal entre no diretório ./frontend
2. No terminal  digite: yarn dev
3. Caso o yarn dev não funcione inicie o projeto com ''ng serve''

### O Projeto iniciará

- Container MySQL
- Container Backend
- Server Front ( sem container )

OBS: 

Existe um diretório no backend chamado 'Test' para utilizar os arquivos de teste instale
no vscode a extensão 'REST Cliente'

### A rota para inclusão de pontos atualiza os dados de positions.json

#### Se você já tiver o MYSQL instalado em seu computador, aconselho pausa-lo para não dar conflitos de porta com o container

```sh
sudo systemctl stop mysql
```

### Por fim, faça o cadastro do seu usário para poder se logar no sistema
