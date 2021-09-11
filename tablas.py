
from peewee import *
import os

os.system("cls")

myDB = SqliteDatabase('Anime.db')


class Anime(Model):
    nombre = CharField(100)
    estado = CharField(50)
    genero = TextField()
    class Meta:
        database = myDB

class Personajes(Model):
    nombre = CharField(50)
    apellido = CharField(50)
    foto_url = TextField()
    serie_F_K = ForeignKeyField(Anime, backref= "Serie")
    pornunciacion = CharField(100)
    fecha_nacimiento = CharField(50)
    poder = CharField(100)
    frase_favorita = CharField(100)
    vestimenta = TextField()
    genero = CharField(100)
    edad = CharField(50)
    altura = CharField(15)
    sexo = CharField(5)
    estado = CharField(100)
    direccion = CharField(100)
    latitud = FloatField()
    longitud = FloatField()
    signo_zodiacal = CharField(100)
    class Meta:
        database = myDB


        
myDB.connect()
myDB.create_tables([Personajes, Anime])