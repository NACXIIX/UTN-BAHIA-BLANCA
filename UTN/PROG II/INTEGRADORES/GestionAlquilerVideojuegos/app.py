from flask import Flask
from rutas.rutas_videojuegos import bp_videojuegos
from rutas.rutas_desarrolladoras import bp_desarrolladoras
from rutas.rutas_generos import bp_generos
app = Flask(__name__)

app.register_blueprint(bp_videojuegos)
app.register_blueprint(bp_desarrolladoras)
app.register_blueprint(bp_generos)

if __name__ == '__main__':
    app.run(debug=True, port=8000)