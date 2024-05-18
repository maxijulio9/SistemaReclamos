from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Municipio(Base):
    __tablename__ =  "municipio"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    #connection = engine.connect()
    metadata = MetaData()
    muni = Table("municipio", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, mun_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.muni]).where(cls.muni.c.mun_id == mun_id)
        return query

    @classmethod
    def all_municipalities(cls):
        """
        Cuáles son las municipalidades (en caso de no pasar parámetros)
        """
        query = select([cls.muni])
        return query
   

    @classmethod
    def single_municipality(cls, mun_id):
        """
        Cuáles son las municipalities con el mun_id
        """
        query = select([cls.muni]).where(cls.muni.c.mun_id == mun_id)
        return query

    
    @classmethod
    def single_municipality_by_name(cls, mun_nombre):
        """
        Cuáles son las municipalidades con el mun_nombre igual
        """
        query = select([cls.muni]).where(cls.muni.c.mun_nombre == mun_nombre)
        #result = cls.connection.execute(query).fetchall()
        #if not result:
         #   return "No existen registros para"
        return query

    
    @classmethod
    def municipality_by_province(cls, prov_id):
        """
        Cuáles son las municipalidades por prov_id
        """
        query = select([cls.muni]).where(cls.muni.c.prov_id == prov_id)
        return query

