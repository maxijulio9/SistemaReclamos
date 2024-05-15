import sys
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Estado(Base):
    __tablename__ =  "estado"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    estado = Table("estado", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, est_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.estado]).where(cls.estado.c.est_id == est_id)
        return query
        #return cls.connection.execute(query).fetchall()


    @classmethod
    def all_status(cls):
        """
        Cuáles son las categorias (en caso de no pasar parámetros)
        """
       # connection = cls.engine.connect()
        query = select([cls.estado])
        #result = connection.execute(query).fetchall()
       #connection.close()
        return query
    '''
    @classmethod
    def all_status(cls):
        """
        Cuáles son las categorias (en caso de no pasar parámetros)
        """
        query = select([cls.estado])
        return cls.connection.execute(query).fetchall()
'''
    @classmethod
    def single_status(cls, est_id):
        """
        Cuáles son las estado(solo nombre) con el est_id
        """
       # connection = cls.engine.connect()
        query = select([Estado.est_nombre]).where(cls.estado.c.est_id == est_id)
        #result = connection.execute(query).fetchall()
        #connection.close()
        return query
    
    @classmethod
    def single_status_by_name(cls, est_nombre):
        """
        Cuáles son las status con el est_nombre igual
        """
      #  connection = cls.engine.connect()
        query = select([cls.estado]).where(cls.estado.c.est_nombre == est_nombre)
      #  result = connection.execute(query).fetchall()
       # connection.close()
        return query
