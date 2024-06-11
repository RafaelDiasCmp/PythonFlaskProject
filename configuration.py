from routes.home import home_route
from routes.responsavel import responsavel_route
from database.database import db
from database.models.responsavel import Produto

def configure_all(app):
    configure_routes(app)
    configure_db()



def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(responsavel_route, url_prefix='/responsavel')


def configure_db():
    db.connect()
    db.create_tables([Produto])