from config import app, db
from RoutesReservas import reserva

app.register_blueprint(reserva)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=['DEBUG'])

