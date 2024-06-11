from peewee import Model, CharField, FloatField, DateTimeField
from database.database import db
import datetime

class Produto(Model):
    nome = CharField()
    preco = FloatField()
    qtde = FloatField()
    data_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db