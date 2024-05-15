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
    def get_users(self, *, use_id = None, mun_id = None):
        print("I'm inside of the method")

        if use_id is None:
            print("Los usuarios son: ")
            query =  Usuario.all_users()
        elif(use_id is not None):
            print("Datos del usuario: ")
            query = Usuario.single_usuario(use_id=use_id)   
        return self.connection.execute(query).fetchall() 
    
    @classmethod
    def get_status(self, *, est_id = None):
        print("I'm inside of the method")
        
        if est_id is None:
            print("Los estados posibles son: ")
            query =  Estado.all_status()
        elif(est_id is not None):
            print("Estado seleccionado: ")
            query = Estado.single_status(est_id= est_id)
               
        return self.connection.execute(query).fetchall() 