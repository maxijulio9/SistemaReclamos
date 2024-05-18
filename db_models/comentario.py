from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION
from datetime import date  
from reclamo import Reclamo
from usuario import Usuario


Base = declarative_base()

class Comentario(Base):
    __tablename__ =  "comentario"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
   #connection = engine.connect()
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
        return query
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def all_benefits(cls):
        """
        Cuáles son los beneficios
        """

        query = select([cls.comen])
        return query 
        #return cls.connection.execute(query).fetchall()
    
    @classmethod
    def single_benefit(cls, com_id):
        """
        Cuáles son los comentario por com_id
        """

        query = select([cls.comen]).where(cls.comen.c.com_id == com_id)
        return query
    #   return cls.connection.execute(query).fetchall()

    @classmethod
    def older_comment(cls):
        """
        Cuál es el comentario más antiguo
        """

        query = select([cls.comen]).where(cls.comen.c.com_fecha_creacion <= date.today()).order_by(cls.comen.c.com_fecha_creacion).limit(1)
        return query
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def newer_comment(cls):
        """
        Cuál es el comentario más antiguo
        """

        query = select([cls.comen]).where(cls.comen.c.com_fecha_creacion >= date.today()).order_by(cls.comen.c.com_fecha_creacion).limit(1)
        return query
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def comments_by_claim(cls, rec_id):
        """
        Cuál son los comentarios por reclamo
        """
        
        j = join(
                cls.comen,
                reclamo.Reclamo.rec,
                cls.comen.c.rec_id == reclamo.Reclamo.rec.c.rec_id,
            )
        query = (
                select([Comentario.com_texto, Comentario.com_fecha_creacion, Reclamo.rec_titulo, Reclamo.rec_fecha_creacion])
                .select_from(j)
                .where(cls.comen.c.rec_id == rec_id)
            )
    

    @classmethod
    def comments_by_user(cls, use_id):
        """
        Cuál son los comentarios por usuarios
        """
        
        j = join(
                cls.comen,
                usuario.Usuario.usuario,
                cls.comen.c.use_id ==  usuario.Usuario.usuario.c.use_id,
            )
        query = (
                select([Comentario.com_texto, Comentario.com_fecha_creacion, Usuario.use_nombre, Usuario.use_apellido])
                .select_from(j)
                .where(cls.comen.c.use_id == use_id)
            )
    