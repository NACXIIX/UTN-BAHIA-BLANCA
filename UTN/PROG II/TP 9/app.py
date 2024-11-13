from flask import Flask
from rutas.rutas_libros import bp_libros

#Instanciando la aplicacion FLASK
app = Flask(__name__)

app.register_blueprint(bp_libros)

if __name__ == '__main__':
    app.run(debug=True, port= 5000)