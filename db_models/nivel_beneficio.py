from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

from nivel import Nivel
from beneficio import Beneficio

Base = declarative_base()

class NivelBeneficio(Base):
    __tablename__ =  "nivel_beneficios"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    #connection = engine.connect()
    metadata = MetaData()
    nivelBeneficio = Table("nivel_beneficios", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    '''
    @classmethod
    def parameters_by_id(cls, *, niv_ben_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.nivelBeneficio]).where(cls.nivelBeneficio.c.niv_ben_id == niv_ben_id)
        return query
    '''
    @classmethod
    def all_levels_benefit(cls):
        """
        Cuáles son los nivelesbeneficio (en caso de no pasar parámetros)
        """
        query = select([cls.nivelBeneficio])
        return query
        #return cls.connection.execute(query).fetchall()

    @classmethod
    def single_level_benefit(cls, *, niv_ben_id):
        """
        Cuáles son los niveles con el niv_ben_id
        """
        query = select([cls.nivelBeneficio]).where(cls.nivelBeneficio.c.niv_ben_id == niv_ben_id)
        return query
        #return cls.connection.execute(query).fetchall()
    
    @classmethod
    def benefits_by_level_benefits(cls, *, niv_id):
        """
        Cuáles son los beneficios por nivel
        """
        j = join(
                cls.nivelBeneficio,
                nivel.Nivel.nivels,
                cls.nivelBeneficio.c.niv_id ==  nivel.Nivel.nivels.c.niv_id,
            )\
            .join(
                cls.nivelBeneficio,
                beneficio.Beneficio.bene,
                beneficio.Beneficio.bene.c.ben_id ==  cls.nivelBeneficio.c.ben_id,
            )
        query = (
                select([Nivel.niv_nombre, Beneficio.ben_nombre, Beneficio.ben_descripcion])
                .select_from(j)
                .where(cls.nivelBeneficio.c.niv_id == niv_id)
            )
        return query