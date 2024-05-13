from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Categoria(Base):
    __tablename__ =  "categoria"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    cate = Table("categoria", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, cat_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.cate]).where(cls.cate.c.cat_id == cat_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def all_categorias(cls):
        """
        Cuáles son las categorias (en caso de no pasar parámetros)
        """

        query = select([cls.cate])
        return cls.connection.execute(query).fetchall()


    @classmethod
    def single_categoria(cls, *, cat_id):
        """
        Cuáles son las categoria con el cat_id
        """
        query = select([cls.cate]).where(cls.cate.c.cat_id == cat_id)
        return cls.connection.execute(query).fetchall()

    
    @classmethod
    def single_categoria_by_name(cls, *, cat_nombre):
        """
        Cuáles son las categoria con el cat_nombre igual
        """
        query = select([cls.cate]).where(cls.cate.c.cat_nombre == cat_nombre)
        return cls.connection.execute(query).fetchall()

    
    
'''

class ParametersHospital(Base):
    __tablename__ = "parameters_hospital"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    hos = Table("hospitals", metadata, autoload=True, autoload_with=engine, schema='hca')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, hos_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.hos]).where(cls.hos.c.hos_id == hos_id)
        return query
        
'''