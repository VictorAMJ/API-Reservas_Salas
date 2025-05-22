from flask import Blueprint, request, jsonify
from ModelReservas import criar_reserva, listar_reservas
from config import db
import requests

reserva = Blueprint('reserva', __name__)

def validar_turma(turma_id):
    resposta = requests.get(f"http://127.0.0.1:8080/turma/{turma_id}")
    return resposta.status_code == 200


@reserva.route("/reserva", methods=["POST"])
def rota_criar_reserva():
    try:
        dados = request.json
        turma_id = dados.get("turma_id")
        if not validar_turma(turma_id):
            return jsonify({"erro":"Turma não encontrada"}), 400
        resposta, status_code = criar_reserva(dados)
        return jsonify(resposta), status_code
    except Exception as e:
        return jsonify({"erro": f"Erro indesperado ao criar aluno: {str(e)}"}), 500
    
@reserva.route("/reserva", methods=["GET"])
def rota_listar_reservas():
    try:
        reserva = listar_reservas()
        return jsonify(reserva)
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado ao listar alunos: {str(e)}"}), 500
    