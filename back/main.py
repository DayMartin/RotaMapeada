from flask import Flask, make_response
from controllers.userController import user_controller
from db.database import get_mysql_connection

app = Flask(__name__)

# Chama a função para obter a conexão MySQL
conn = get_mysql_connection()

app.register_blueprint(user_controller)

@app.route('/')
def root():
    return make_response('Servidor Conectado', 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
