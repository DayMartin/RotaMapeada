import mysql.connector
from flask import Flask, request, jsonify
import datetime

def get_mysql_connection():
    # Configuração da conexão
    config = {
        'user': 'root',
        'password': 'Rs5kD85DQk6',
        'host': 'servidor_mysql',
        'database': 'dbrotas',
        'port':'3306'
    }

    # Conectar ao banco de dados
    conn = mysql.connector.connect(**config)

    # Confirmar conexão bem-sucedida
    if conn.is_connected():
        print("Conexão ao banco de dados MySQL bem-sucedida!")
    else:
        print("Erro ao conectar ao banco de dados MySQL.")

    return conn
