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
            # ... (lógica de atualização do aluno)
            return jsonify({"mensagem": "Aluno atualizado com sucesso"}), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 400
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos.route('/alunos/<int:id>', methods=['PUT'])
@swag_from({
    # ... (outras configurações)
})
def atualizar_aluno_interno(id): 
    return atualizar_aluno(id)
