from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION
from datetime import date  


Base = declarative_base()

class Comentario(Base):
    __tablename__ =  "comentario"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    comen = Table("comentario", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *,com_id ):
        """
        Cuáles son los parámetros
        """
        query = select([cls.comen]).where(cls.comen.c.com_id == com_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def all_benefits(cls):
        """
        Cuáles son los beneficios
        """

        query = select([cls.comen])
        return cls.connection.execute(query).fetchall()
    
    @classmethod
    def single_benefit(cls, com_id):
        """
        Cuáles son los comentario por com_id
        """

        query = select([cls.comen]).where(cls.comen.c.com_id == com_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def older_comment(cls):
        """
        Cuál es el comentario más antiguo
        """

        query = select([cls.comen]).where(cls.comen.c.com_fecha_creacion <= date.today()).order_by(cls.comen.c.com_fecha_creacion).limit(1)
        return cls.connection.execute(query).fetchall()

    
