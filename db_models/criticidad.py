from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Criticidad(Base):
    __tablename__ =  "criticidad"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    #connection = engine.connect()
    metadata = MetaData()
    criticidad = Table("criticidad", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, cri_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.criticidad]).where(cls.criticidad.c.est_id == cri_id)
        return query 
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def all_criticities(cls):
        """
        Cuáles son las categorias (en caso de no pasar parámetros)
        """
        query = select([cls.criticidad])
        return query
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def single_criticities(cls, *, cri_id):
        """
        Cuáles son las criticidades con el cri_id
        """
        query = select([cls.criticidad]).where(cls.criticidad.c.cri_id == cri_id)
        return query
        #return cls.connection.execute(query).fetchall()
    
    @classmethod
    def single_criticity_by_name(cls, *, cri_nombre):
        """
        Cuáles son las status con el est_nombre igual
        """
        query = select([cls.criticidad]).where(cls.criticidad.c.cri_nombre == cri_nombre)
        return query
        #return cls.connection.execute(query).fetchall()
