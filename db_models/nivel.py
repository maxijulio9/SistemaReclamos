from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select, join
from config_vars import BBDD_CONNECTION

from nivel_beneficio import NivelBeneficio
from beneficio import Beneficio

Base = declarative_base()

class Nivel(Base):
    __tablename__ =  "nivel"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    metadata = MetaData()
    nivels = Table("nivel", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *, niv_id):
        """
        Cuáles son los parámetros
        """
        query = select([cls.nivels]).where(cls.nivels.c.niv_id == niv_id)
        return cls.connection.execute(query).fetchall()

    @classmethod
    def all_levels(cls):
        """
        Cuáles son los niveles (en caso de no pasar parámetros)
        """
        query = select([cls.nivels])
        return cls.connection.execute(query).fetchall()

    @classmethod
    def single_level(cls, *, niv_id):
        """
        Cuáles son los niveles con el niv_id
        """
        query = select([cls.nivels]).where(cls.nivels.c.niv_id == niv_id)
        return cls.connection.execute(query).fetchall()
    
    @classmethod
    def single_level_by_name(cls, *, niv_nombre):
        """
        Cuáles son los niveles con el niv_nombre igual
        """
        query = select([cls.nivels]).where(cls.nivels.c.niv_nombre == niv_nombre)

        return cls.connection.execute(query).fetchall()
    

    '''--consulta los beneficios por nivel
    SELECT  n.NIV_NOMBRE, b.BEN_NOMBRE, b.BEN_DESCRIPCION 
    FROM NIVEL n
	    JOIN NIVEL_BENEFICIOS nb  ON n.NIV_ID  = nb.NIV_ID
	    JOIN BENEFICIOS b ON b.BEN_ID  = nb.BEN_ID 
    WHERE  n.NIV_ID =1;'''

    @classmethod
    def benefics_by_level(cls, *, niv_id):
        """
        Cuáles son los beneficios por nivel
        """
        j = join(
                cls.nivels,
                nivel_beneficio.NivelBeneficio.nivelBeneficio,
                cls.nivels.c.niv_id ==  nivel_beneficio.NivelBeneficio.nivelBeneficio.c.niv_id,
            )\
            .join(
                nivel_beneficio.NivelBeneficio.nivelBeneficio,
                beneficio.Beneficio.bene,
                beneficio.Beneficio.bene.c.ben_id ==  nivel_beneficio.NivelBeneficio.nivelBeneficio.c.ben_id,
            )
        query = (
                select([Nivel.niv_nombre, Beneficio.ben_nombre, Beneficio.ben_descripcion])
                .select_from(j)
                .where(cls.nivels.c.niv_id == niv_id)
            )
        
        return cls.connection.execute(query).fetchall()

        '''
        query = select([Nivel.niv_nombre, Beneficio.ben_nombre, Beneficio.ben_descripcion]) \
                    .select_from(join(Nivel, NivelBeneficio, Nivel.niv_id == NivelBeneficios.niv_id)) \
                    .join(Beneficio, Beneficio.ben_id == NivelBeneficio.ben_id) \
                 .where(Nivel.niv_id == niv_id)

        return query
        '''
        