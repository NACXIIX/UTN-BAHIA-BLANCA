from flask import Flask
from routes.routes_videojuegos import bp_videojuegos
from routes.routes_desarrolladoras import bp_desarrolladoras
from routes.routes_generos import bp_generos
from routes.principal_route import bp_main_route

app = Flask(__name__, template_folder="views/templates", static_folder="views/static")
app.register_blueprint(bp_main_route)
app.register_blueprint(bp_videojuegos)
app.register_blueprint(bp_desarrolladoras)
app.register_blueprint(bp_generos)

if __name__ == '__main__':
    app.run(debug=True, port=8000)