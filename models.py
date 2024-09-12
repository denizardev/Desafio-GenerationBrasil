from db_config import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    nome_professor = db.Column(db.String(100), nullable=False)
    numero_sala = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "nota_primeiro_semestre": self.nota_primeiro_semestre,
            "nota_segundo_semestre": self.nota_segundo_semestre,
            "nome_professor": self.nome_professor,
            "numero_sala": self.numero_sala
        }
