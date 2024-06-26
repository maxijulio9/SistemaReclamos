--El presente script tiene los scripts de los objetos de la base de datos

CREATE TABLE BENEFICIOS (
    BEN_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    nombre VARCHAR(30),
    descripcion VARCHAR(100),
    fecha_de_inicio DATE,
    fecha_de_expiracion DATE   
);

alter table BENEFICIOS  add constraint "BEN_PK" primary key (BEN_ID);

--DROP TABLE BENEFICIOS ;
--SELECT constraint_name, constraint_type
--FROM user_constraints
--WHERE table_name = 'NIVEL_BENEFICIOS';


--SELECT * FROM USER_TABLES ;

--SELECT constraint_name, constraint_type
--FROM user_constraints
--WHERE table_name = 'BENEFICIOS';

--DROP TABLE NIVEL ;
DROP TABLE USUARIO ;
CREATE TABLE NIVEL (
    NIV_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    nombre VARCHAR(30),
    descripcion varchar(250)
   
);

alter table NIVEL  add constraint "NIV_PK" primary key (NIV_ID);

CREATE TABLE NIVEL_BENEFICIOS (
    NIV_BEN_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    NIV_ID NUMBER(10) NOT NULL,
    BEN_ID NUMBER(10) NOT NULL
);

alter table NIVEL_BENEFICIOS  add constraint "NIV_BEN_PK" primary key (NIV_BEN_ID);
--alter table NIVEL add constraint "NIV_NIV_BEN_FK" foreign key (NIV_ID) references NIVEL(NIV_ID);

alter table NIVEL_BENEFICIOS add constraint "NIV_BEN_BEN_FK" foreign key (BEN_ID) references BENEFICIOS(BEN_ID);
alter table NIVEL_BENEFICIOS add constraint "NIV_BEN_NIV_FK " foreign key (NIV_ID) references NIVEL(NIV_ID);

CREATE TABLE PROVINCIA (
    PROV_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    nombre VARCHAR(30),
    direccion VARCHAR(50)
);

alter table PROVINCIA add constraint "PROV_PK" primary key (PROV_ID);

CREATE TABLE MUNICIPIO (
    MUN_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    PROV_ID NUMBER(10) NOT NULL,
    nombre VARCHAR(30)
);

alter table MUNICIPIO add constraint "MUN_PK" primary key (MUN_ID);
alter table MUNICIPIO add constraint "MUN_PROV_FK" foreign key (PROV_ID) references PROVINCIA(PROV_ID);


CREATE TABLE USUARIO (
    USE_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    MUN_ID NUMBER(10) NOT NULL,
    NIV_BEN_ID NUMBER(10) NOT NULL,
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    correo VARCHAR(30),
    telefono VARCHAR(30),
    DNI VARCHAR(30),
    contrasenia VARCHAR(30)
);

alter table USUARIO add constraint "USE_PK" primary key (USE_ID);
alter table USUARIO add constraint "USE_NIV_FK" foreign key (NIV_BEN_ID) references NIVEL_BENEFICIOS(NIV_BEN_ID);
alter table USUARIO add constraint "USE_MUN_FK" foreign key (MUN_ID) references  MUNICIPIO(MUN_ID);
---ALTER TABLE USUARIO MODIFY correo VARCHAR(50);
 


CREATE TABLE ESTADO (
    EST_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    nombre VARCHAR(30),
    descripcion VARCHAR(250)
);
alter table estado add constraint "EST_PK" primary key (EST_ID);

CREATE TABLE CRITICIDAD (
    CRI_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    nombre VARCHAR(30),
    descripcion VARCHAR(250)
);
alter table CRITICIDAD  add constraint "CRI_PK" primary key (CRI_ID);



CREATE TABLE GESTOR (
    GES_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    correo VARCHAR(30),
    telefono VARCHAR(30),
    DNI VARCHAR(30),
    contrasenia VARCHAR(30)
);

alter table GESTOR  add constraint "GES_PK" primary key (GES_ID);



CREATE TABLE CATEGORIA (
    CAT_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    nombre VARCHAR(30)
);

alter table CATEGORIA  add constraint "CAT_PK" primary key (CAT_ID);
------------------------------- ---------------------------------------


CREATE TABLE UBICACION (
    UBI_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    latitud VARCHAR(50),
    longitud VARCHAR(50),
    direccion VARCHAR(50)
);
alter table UBICACION  add constraint "UBI_PK" primary key (UBI_ID);





CREATE TABLE RECLAMO (
    REC_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    CAT_ID NUMBER(10) NOT NULL,
    USE_ID NUMBER(10) NOT NULL,
    UBI_ID NUMBER(10) NOT NULL,
    EST_ID NUMBER(10) NOT NULL,
    CRI_ID NUMBER(10) NOT NULL,
    titulo VARCHAR(30),
    descripcion VARCHAR(250),
    fecha_creacion DATE,
    fecha_actualizacion DATE
    --CONSTRAINT REC_PK PRIMARY KEY (REC_ID),
    --CONSTRAINT REC_CAT_FK FOREIGN KEY(CAT_ID) REFERENCES CATEGORIA(CAT_ID),
    --CONSTRAINT REC_USE_FK FOREIGN KEY(USE_ID) REFERENCES USUARIO(USE_ID),
--    CONSTRAINT REC_UBI_FK FOREIGN KEY(UBI_ID) REFERENCES UBICACION(UBI_ID),
   -- CONSTRAINT REC_EST_FK FOREIGN KEY(EST_ID) REFERENCES ESTADO(EST_ID),
    --CONSTRAINT REC_CRI_FK FOREIGN KEY(CRI_ID) REFERENCES CRITICIDAD(CRI_ID)
);

alter table RECLAMO  add constraint "REC_PK" primary key (REC_ID);

alter table RECLAMO add constraint "REC_CAT_FK" foreign key (CAT_ID) references CATEGORIA(CAT_ID);
alter table RECLAMO add constraint "REC_USE_FK" foreign key (USE_ID) references USUARIO(USE_ID);
alter table RECLAMO add constraint "REC_UBI_FK" foreign key (UBI_ID) references UBICACION(UBI_ID);
alter table RECLAMO add constraint "REC_EST_FK" foreign key (EST_ID) REFERENCES ESTADO(EST_ID);
alter table RECLAMO add constraint "REC_CRI_FK" foreign key (CRI_ID) references CRITICIDAD(CRI_ID);


CREATE TABLE COMENTARIO (
    COM_ID NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY NOT NULL,
    REC_ID NUMBER(10) NOT NULL,
    GES_ID NUMBER(10) NOT NULL,
    USE_ID NUMBER (10) NOT NULL,
    fecha_creacion DATE,
    fecha_actualizacion DATE,
    texto VARCHAR(250)
    --CONSTRAINT COM_PK PRIMARY KEY (COM_ID),
    --CONSTRAINT COM_GES_FK FOREIGN KEY(GES_ID) REFERENCES GESTOR(GES_ID),
    --CONSTRAINT COM_USE_FK FOREIGN KEY(USE_ID) REFERENCES USUARIO(USE_ID)
   );
alter table COMENTARIO  add constraint "COM_PK" primary key (COM_ID);
alter table COMENTARIO add constraint "COM_GES_FK" foreign key (GES_ID) REFERENCES GESTOR(GES_ID);
alter table COMENTARIO add constraint "COM_USE_FK" foreign key (USE_ID) REFERENCES USUARIO(USE_ID);


-------------HASTA ACA TODO BIEN(espero)!!---------


