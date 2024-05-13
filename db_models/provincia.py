from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Provincia(Base):
    
    __tablename__ =  "PROVINCIA"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    provincia = Table("PROVINCIA", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, prov_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.provincia]).where(cls.provincia.c.prov_id == prov_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def all_provincias(cls):
        """
        Cuáles son las provincias (en caso de no pasar parámetros)
        """
        query = select([cls.provincia])
        return cls.connection.execute(query).fetchall()

    @classmethod
    def single_provincia(cls, *, prov_id):
        """
        Cuáles son las provincias con el prov_id
        """
        query = select([cls.provincia]).where(cls.provincia.c.prov_id == prov_id)
        return cls.connection.execute(query).fetchall()
    
    @classmethod
    def single_provincia_by_name(cls, *, prov_nombre):
        """
        Cuáles son las provincia con el prov_nombre igual
        """
        query = select([cls.provincia]).where(cls.provincia.c.prov_nombre == prov_nombre)
        return cls.connection.execute(query).fetchall()
