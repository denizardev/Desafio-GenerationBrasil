from flask import Blueprint, request, jsonify
from flasgger import swag_from
from models import Aluno
from db_config import db

alunos = Blueprint('alunos', __name__)

# ... (outros endpoints)

@alunos.route('/alunos', methods=['POST'])
@swag_from({
    # ... (outras configurações)
    'parameters': [
        {
            'name': 'body',
            'description': 'Dados do aluno',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'idade': {'type': 'integer'},
                    'nota_primeiro_semestre': {'type': 'number'},
                    'nota_segundo_semestre': {'type': 'number'},
                    'nome_professor': {'type': 'string'},
                    'numero_sala': {'type': 'integer'}  # Alterado para integer
                },
                'required': ['nome', 'idade']
            }
        }
    ],
    # ... (outras configurações)
})
def cria_aluno():
    body = request.get_json()
    try:
        novo_aluno = Aluno(
            nome=body['nome'],
            idade=body['idade'],
            nota_primeiro_semestre=body['nota_primeiro_semestre'],
            nota_segundo_semestre=body['nota_segundo_semestre'],
            nome_professor=body['nome_professor'],
            numero_sala=int(body['numero_sala'])  # Converte para inteiro
        )
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify(novo_aluno.to_json()), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

# ... (outros endpoints)

@alunos.route('/alunos', methods=['GET'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Lista todos os alunos',
    'responses': {
        '200': {
            'description': 'Lista de alunos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'idade': {'type': 'integer'},
                        'nota_primeiro_semestre': {'type': 'number'},
                        'nota_segundo_semestre': {'type': 'number'},
                        'nome_professor': {'type': 'string'},
                        'numero_sala': {'type': 'integer'}  # Alterado para integer
                    }
                }
            }
        }
    }
})
def lista_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_json() for aluno in alunos]), 200

# ... (outros endpoints)

@alunos.route('/alunos/<int:id>', methods=['GET'])
@swag_from({
    # ... (outras configurações)
    'responses': {
        '200': {
            'description': 'Aluno encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'idade': {'type': 'integer'},
                    'nota_primeiro_semestre': {'type': 'number'},
                    'nota_segundo_semestre': {'type': 'number'},
                    'nome_professor': {'type': 'string'},
                    'numero_sala': {'type': 'integer'}  # Alterado para integer
                }
            }
        },
        '404': {
            'description': 'Aluno não encontrado'
        }
    }
})
def buscar_aluno(id):
    # ... (resto do código)

@alunos.route('/alunos/<int:id>', methods=['PUT'])
@swag_from({
    # ... (outras configurações)
    'parameters': [
        # ... (outros parâmetros)
        {
            'name': 'body',
            'description': 'Dados atualizados do aluno',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'idade': {'type': 'integer'},
                    'nota_primeiro_semestre': {'type': 'number'},
                    'nota_segundo_semestre': {'type': 'number'},
                    'nome_professor': {'type': 'string'},
                    'numero_sala': {'type': 'integer'}  # Alterado para integer
                }
            }
        }
    ],
    # ... (outras configurações)
})
def atualizar_aluno(id):
    # ... (resto do código)

# ... (outros endpoints)