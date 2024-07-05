from peewee import Model, CharField, ForeignKeyField
from database.database import db
from database.models.responsavel import Produto

class Barraca(Model):
    nome = CharField()
    responsavel = CharField()

    class Meta:
        database = db

class ProdutoBarraca(Model):
    produto = ForeignKeyField(Produto, backref='barracas')
    barraca = ForeignKeyField(Barraca, backref='produtos')

    class Meta:
        database = db
