import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")
from sqlalchemy import create_engine, select, join, MetaData, Table

from db_models.beneficio import Beneficio
from db_models.categoria import Categoria
from db_models.estado import Estado
from db_models.nivel import Nivel
from db_models.nivel_beneficio import NivelBeneficio
from db_models.criticidad import Criticidad
from db_models.gestor import Gestor
from db_models.municipio import Municipio
from db_models.provincia import Provincia
from db_models.reclamo import Reclamo
from db_models.comentario import Comentario
from db_models.usuario import Usuario

from config_vars import BBDD_CONNECTION

class ReclamoDAO:
    print("starting")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    print("finished connection")
    metadata = MetaData()

    #a partir de acá los metodos de dao consumiendo los metodos de las clases importadas.

    @classmethod
    def all_users():
        users = Usuario.all_users;
        for u in users:
            print (users[u])
