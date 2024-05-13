from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION


Base = declarative_base()

class Gestor(Base):
    __tablename__ =  "gestor"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    gestor = Table("gestor", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")

    @classmethod
    def all_gestors(cls):
        """
            Cuáles son los gestores en la db
        """
        query = select([cls.gestor])
        return cls.connection.execute(query).fetchall()

    @classmethod
    def single_gestor(cls, *, ges_id):
        """
            Cual es el gestor por ges_id
        """
        query = select([cls.gestor]).where(cls.gestor.c.ges_id == ges_id)
        return cls.connection.execute(query).fetchall()
