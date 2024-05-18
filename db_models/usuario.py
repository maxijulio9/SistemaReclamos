from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select, join, and_
from config_vars import BBDD_CONNECTION

from municipio import Municipio
from nivel import Nivel
from nivel_beneficio import NivelBeneficio
from beneficio import Beneficio


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
    def single_user_by_id(cls, use_id):
        """
            Cual es el usuario por use_id
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_id == use_id)
        return query
    
    @classmethod
    def user_by_dni(cls, use_dni):
        """
            Cual es el usuario por use_dni
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_dni == use_dni)
        return query
    
    @classmethod
    def user_by_name(cls, use_nombre):
        """
            Cual es el usuario por use_nombre
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_nombre == use_nombre)
        return query
    
    @classmethod
    def user_by_lastname(cls, use_apellido):
        """
            Cual es el usuario por use_apellido
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_apellido == use_apellido)
        return query
    
    @classmethod
    def user_by_mail(cls, use_correo):
        """
            Cual es el usuario por use_correo
        """
        query = select([cls.usuario]).where(cls.usuario.c.use_correo == use_correo)
        return query
      

    @classmethod
    def user_by_municipality(cls, mun_id):
        """
            Cual es el usuario por use_id
        """
        j = join(
                cls.usuario,
                Municipio.muni,
                cls.usuario.c.mun_id ==  Municipio.muni.c.mun_id,
            )
        query =(
                 select([cls.usuario, Municipio.mun_nombre])\
                .select_fro(j)
                .where(cls.usuario.c.mun_id == mun_id)
            )

        '''query = select([cls.usuario]) \
                .select_from(Usuario, Ubicacion, Usuario.id_not_in_db = )
                .where(cls.usuario.c.use_id == use_id)
        '''
        return query
        #return cls.connection.execute(query).fetchall()
    
    @classmethod
    def user_level_and_benefits(cls, use_id, use_nombre):
        """
        Cuáles es el nivel del usuario y el beneficio
        """
        j = join(
                cls,
                nivel_beneficio.NivelBeneficio.nivelBeneficio,
                cls.usuario.c.niv_ben_id ==  nivel_beneficio.NivelBeneficio.nivelBeneficio.c.niv_ben_id
        ).join(
                nivel_beneficio.NivelBeneficio.nivelBeneficio,
                nivel.Nivel.nivels,
                nivel_beneficio.NivelBeneficio.nivelBeneficio.c.niv_id == nivel.Nivel.nivels.c.niv_id
        ).join(
                nivel_beneficio.NivelBeneficio.nivelBeneficio,
                beneficio.Beneficio.bene,
                nivel_beneficio.NivelBeneficio.nivelBeneficio.c.ben_id == beneficio.Beneficio.bene.c.ben_id
        )
        
        query = (
                select([Usuario.use_dni, Usuario.use_nombre,  Nivel.niv_nombre, Beneficio.ben_nombre, Beneficio.ben_descripcion])
                .select_from(j)
                .where(
                    and_(
                    cls.usuario.c.use_id == use_id,
                    cls.usuario.c.use_nombre == use_nombre
                    )
                )
            )
        return query