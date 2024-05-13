from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION



Base = declarative_base()

class Ubicacion(Base):
    __tablename__ =  "ubicacion"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    ubi = Table("ubicacion", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    

    @classmethod
    def all_ubication(cls):
        """
        Cuáles son las ubicaciones
        """

        query = select([cls.ubi])
        return cls.connection.execute(query).fetchall()
    
    @classmethod
    def single_benefit(cls, ubi_id):
        """
        Cuáles son los beneficios por ben_id
        """

        query = select([Ubicacion.ubi_latitud,Ubicacion.ubi_longitud,Ubicacion.ubi_direccion]).where(cls.ubi.c.ubi_id == ubi_id)
        return cls.connection.execute(query).fetchall()
