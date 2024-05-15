from flask import Flask
from routes.home import home_route
from routes.responsavel import responsavel_route

# Inicialização
app = Flask(__name__)

# Rotas
app.register_blueprint(home_route)
app.register_blueprint(responsavel_route, url_prefix='/responsavel')



# Execução
app.run(debug=True)