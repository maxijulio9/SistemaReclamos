from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

from municipio import Municipio


Base = declarative_base()

class Usuario(Base):
    __tablename__ =  "usuario"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    #connection = engine.connect()
    metadata = MetaData()
    usuario = Table("usuario", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")

    @classmethod
    def all_users(cls):
        """
            Cuáles son los usuarios en la db
        """
        query = select([cls.usuario])
        return query
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def single_usuario(cls, use_id):
        """
            Cual es el usuario por use_id
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_id == use_id)
        return query
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def user_by_municipality(cls, *, use_id):
        """
            Cual es el usuario por use_id
        """
        j = join(
                cls.usuario,
                municipio.Municipio.muni,
                cls.usuario.c.mun_id ==  municipio.Municipio.muni.c.mun_id,
            )
        query =(
                 select([cls.usuario, Municipio.mun_nombre])\
                .select_from(j)
            )

        '''query = select([cls.usuario]) \
                .select_from(Usuario, Ubicacion, Usuario.id_not_in_db = )
                .where(cls.usuario.c.use_id == use_id)
        '''
        return query
        #return cls.connection.execute(query).fetchall()
