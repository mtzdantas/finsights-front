from . import db
from datetime import date

class Extrato(db.Model):
    __tablename__ = 'extrato'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    tipo_lancamento = db.Column(db.Text, nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    doc_destinatario = db.Column(db.String(20))
    nome_destinatario = db.Column(db.Text)
    usuario_id = db.Column(db.String(80), nullable=False)
    arquivo_id = db.Column(db.String, nullable=False)
