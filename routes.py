from flask import Blueprint, request, jsonify
from models import Aluno
from db_config import db

alunos = Blueprint('alunos', __name__)

@alunos.route('/alunos', methods=['POST'])
def cria_aluno():
    body = request.get_json()
    try:
        novo_aluno = Aluno(
            nome=body['nome'],
            idade=body['idade'],
            nota_primeiro_semestre=body['nota_primeiro_semestre'],
            nota_segundo_semestre=body['nota_segundo_semestre'],
            nome_professor=body['nome_professor'],
            numero_sala=body['numero_sala']
        )
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify(novo_aluno.to_json()), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@alunos.route('/alunos', methods=['GET'])
def lista_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_json() for aluno in alunos]), 200

@alunos.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno:
        return jsonify(aluno.to_json()), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    body = request.get_json()
    aluno = Aluno.query.get(id)
    if aluno:
        try:
            aluno.nome = body.get('nome', aluno.nome)
            aluno.idade = body.get('idade', aluno.idade)
            aluno.nota_primeiro_semestre = body.get('nota_primeiro_semestre', aluno.nota_primeiro_semestre)
            aluno.nota_segundo_semestre = body.get('nota_segundo_semestre', aluno.nota_segundo_semestre)
            aluno.nome_professor = body.get('nome_professor', aluno.nome_professor)
            aluno.numero_sala = body.get('numero_sala', aluno.numero_sala)
            
            db.session.commit()
            return jsonify(aluno.to_json()), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 400
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if aluno:
        try:
            db.session.delete(aluno)
            db.session.commit()
            return jsonify(aluno.to_json()), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 400
    return jsonify({"erro": "Aluno não encontrado"}), 404
