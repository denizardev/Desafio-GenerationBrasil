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
    # ... (código da função cria_aluno)

# ... (outros endpoints)
    @alunos.route('/alunos/<int:id>', methods=['GET'])
    @swag_from({
    # ... (outras configurações)
})
    def buscar_aluno(id):
    # ... (código da função buscar_aluno)

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
            
            # Certifique-se de converter para inteiro, mesmo que o valor venha do objeto 'aluno'
            aluno.numero_sala = int(body.get('numero_sala', aluno.numero_sala)) 

            db.session.commit()
            return jsonify(aluno.to_json()), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 400
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos.route('/alunos/<int:id>', methods=['PUT'])  # Rota PUT dentro da função atualizar_aluno
@swag_from({
    # ... (outras configurações)
})
def atualizar_aluno_interno(id):  # Função interna para lidar com a rota PUT
    return atualizar_aluno(id)  # Chama a função externa para processar a lógica

# ... (outros endpoints)