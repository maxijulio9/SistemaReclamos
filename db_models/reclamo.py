import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select, join
from config_vars import BBDD_CONNECTION
from datetime import date  

from . import municipio


Base = declarative_base()

class Reclamo(Base):
    __tablename__ =  "reclamo"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    #connection = engine.connect()
    metadata = MetaData()
    rec = Table("reclamo", metadata, autoload=True, autoload_with=engine, schema='claim')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def parameters_by_id(cls, *,rec_id ):
        """
        Cuáles son los parámetros
        """
        query = select([cls.rec]).where(cls.rec.c.rec_id == rec_id)
        return query
    #return cls.connection.execute(query).fetchall()

    @classmethod
    def all_claims(cls):
        """
        Cuáles son los beneficios
        """

        query = select([cls.rec])
        return query
    #return cls.connection.execute(query).fetchall()
    
    @classmethod
    def single_claim(cls, rec_id):
        """
        Cuáles son los reclamos por rec_id
        """

        query = select([cls.rec]).where(cls.rec.c.rec_id == rec_id)
        return query#return cls.connection.execute(query).fetchall()
    
    '''
    Select rec.nombre, rec.descripcion, m.nombre
    from reclamo rec
        join municipio m on m.mun_id = rec.mun_id
    where m.mun_id = m.mun_id
    '''
    
    @classmethod
    def claims_by_municipality(cls, mun_id):
        """
        Cuáles son los reclamos por municipio
        """
        j = join(
                cls.rec,
                municipio.Municipio.muni,
                cls.rec.c.mun_id ==  municipio.Municipio.muni.c.mun_id,
            )
        query = (
                select([cls.rec.c.rec_titulo, cls.rec.c.rec_descripcion, municipio.Municipio.muni.c.mun_nombre ])
                .select_from(j)
                .where(cls.rec.c.mun_id == mun_id)
            )
        
        '''result =cls.connection.execute(query).fetchall()
        if not result:
            return "No existen registros de reclamos para el municipio con id {}".format(mun_id)
        return result
'''
        return query