from config import db

class Reservas(db.Model):
    __tablename__ = "reservas"

    id = db.Column(db.Integer, primary_key=True)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    turma_id = db.Column(db.String(5), nullable=False)

    def __init__(self, sala, data, periodo, turma_id):
        self.sala = sala
        self.data = data
        self.periodo = periodo 
        self.turma_id = turma_id

    def transformar_em_dic(self):
        return{
            'id':self.id,
            'sala':self.sala,
            'data':self.data,
            'periodo':self.periodo,
            'turma_id':self.turma_id
        }


def criar_reserva(dados):
    nova_reserva = Reservas(
        sala = dados["sala"],
        data = dados["data"],
        periodo = dados["periodo"],
        turma_id = int(dados["turma_id"])
    )

    db.session.add(nova_reserva)
    db.session.commit()
    return{"mensagem":"Reserva feita com sucesso!"}, 201

def listar_reservas():
    reservas = Reservas.query.all()
    print(reservas)
    return[reserva.transformar_em_dic() for reserva in reservas]
