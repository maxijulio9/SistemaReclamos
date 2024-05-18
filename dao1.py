import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")
from sqlalchemy import create_engine, select, join, MetaData, Table

from db_models.beneficio import Beneficio
from db_models.categoria import Categoria
from db_models.estado import Estado
from db_models.nivel import Nivel
from db_models.nivel_beneficio import NivelBeneficio
from db_models.criticidad import Criticidad
from db_models.gestor import Gestor
from db_models.municipio import Municipio
from db_models.provincia import Provincia
from db_models.reclamo import Reclamo
from db_models.comentario import Comentario
from db_models.usuario import Usuario

from config_vars import BBDD_CONNECTION

class ReclamoDAO:
    print("starting")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    print("finished connection")
    metadata = MetaData()

    #a partir de acá los metodos de dao consumiendo los metodos de las clases importadas.

    def hi_test(self):
        print("Hola mundo")

    #beneficios
    def get_benefits(self,*,ben_id=None):

        single_mode = ben_id is not None
        if single_mode:
            query = Beneficio.single_benefit(ben_id=ben_id)
        else:
            query = Beneficio.all_benefits()
        return self.connection.execute(query).fetchall()

    def get_benefits_closest_to_expiration(self):
        query = Beneficio.benefit_closest_to_expiration()
        return self.connection.execute(query).fetchall()
    
    #categoria
    def get_categories(self,*,cat_id=None):
        
        single_mode = cat_id is not None
        if single_mode:
            query = Categoria.single_category(cat_id=cat_id)#cambio
        else:
            query = Categoria.all_categories()#cambio
        return self.connection.execute(query).fetchall()
        
    def get_categories_by_name(self,*,nombre):
        query = Categoria.single_categoria_by_name(nombre)
        return self.connection.execute(query).fetchall()
    
    #estado
    def get_status(self,*,est_id=None):
        
        single_mode = est_id is not None
        if single_mode:
            query = Estado.single_status(est_id=est_id)
        else:
            query = Estado.all_status()
        return self.connection.execute(query).fetchall()
        
    def get_statu_by_name(self,*,nombre):
        query = Estado.single_status_by_name(nombre)
        return self.connection.execute(query).fetchall()

    #nivel
    def get_levels(self,*,niv_id=None):
        
        single_mode = niv_id is not None
        if single_mode:
            query = Nivel.single_level(niv_id=niv_id)
        else:
            query = Nivel.all_levels()
        return self.connection.execute(query).fetchall()
        
    def get_level_by_name(self,*,nombre):
        query = Nivel.single_level_by_name(nombre)
        return self.connection.execute(query).fetchall()

    #!falta beneficios por nivel¡#

    #nivel-beneficio
    def get_levels_benfits(self,*,niv_ben_id=None):
        
        single_mode = niv_ben_id is not None
        if single_mode:
            query = NivelBeneficio.single_level_benefit(niv_ben_id=niv_ben_id)
        else:
            query = NivelBeneficio.all_levels_benefit()
        return self.connection.execute(query).fetchall()
    #criticidad
    def get_criticities(self,*,cri_id=None):
        
        single_mode = cri_id is not None
        if single_mode:
            query = Criticidad.single_criticities(cri_id=cri_id)
        else:
            query = Criticidad.all_criticities()
        return self.connection.execute(query).fetchall()
        
    def get_criticities_by_name(self,*,nombre):
        query = Criticidad.single_criticity_by_name(nombre)
        return self.connection.execute(query).fetchall()
    #gestor
    def get_managers(self,*,ges_id=None):
        
        single_mode = ges_id is not None
        if single_mode:
            query = Gestor.single_manager(ges_id=ges_id)#cambio 
        else:
            query = Gestor.all_managers()#cambio
        return self.connection.execute(query).fetchall()
    #municipio
    def get_municipalities(self,*,mun_id=None):
        
        single_mode = mun_id is not None
        if single_mode:
            query = Municipio.single_municipality(mun_id=mun_id)
        else:
            query = Municipio.all_municipalities()
        return self.connection.execute(query).fetchall()
        #!falta muni por prov¡#
        #!falta munu por nombre¡#
    #provincia 
    def get_province(self,*,prov_id=None):
        single_mode = prov_id is not None
        if single_mode:
            query = Provincia.single_province(prov_id=prov_id)#cambio
        else:
            query = Provincia.all_provinces()#cambio
        return self.connection.execute(query).fetchall()
    def get_province_by_name(self,*,nombre):
        query = Provincia.single_provincia_by_name(nombre)
        return self.connection.execute(query).fetchall()
    #reclamo
    def get_claims(self,*,rec_id=None):
        single_mode = rec_id is not None
        if single_mode:
            query = Reclamo.single_claim(rec_id=rec_id)
        else:
            query = Reclamo.all_claims()
        return self.connection.execute(query).fetchall()
        #!reclamos por muni¡
    #comentario
    def get_comments(self,*,com_id=None):
        single_mode = com_id is not None
        if single_mode:
            query = Comentario.single_comment(com_id=com_id)
        else:
            query = Comentario.all_coments()
        return self.connection.execute(query).fetchall()
        #!falta comentario mas viejo¡
    #usuario
    def get_users(self,*,com_id=None):
        single_mode = use_id is not None
        if single_mode:
            query = Usuario.single_user(use_id=use_id)
        else:
            query = Usuario.all_users()
        return self.connection.execute(query).fetchall()
        #falta usuario por municipalidad
        
        

