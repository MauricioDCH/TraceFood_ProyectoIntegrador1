CREATE TABLE PROVEEDOR(
  proveedor_ID varchar(20) NOT NULL UNIQUE,
  rol int NOT NULL,
  nombre varchar(20) NOT NULL,
  apellido varchar(20) NOT NULL,
  correo varchar(50) NOT NULL,
  telefono varchar(10) NOT NULL,
  direccion varchar(20) NOT NULL,
  Municipio varchar (20) NOT NULL,
  Departamento varchar (20) NOT NULL,
  Pais varchar (20) NOT NULL,
  Cartificaciones boolean NOT NULL,
  
  CONSTRAINT pk_proveedor PRIMARY KEY (proveedor_ID)
);

CREATE TABLE RES(
 res_ID varchar(20) NOT NULL UNIQUE,
 fecha_nacimiento date NOT NULL,
 fecha_muerte date,
  peso_kg float NOT NULL,
  estado varchar(20) NOT NULL,
  comentarios varchar(200),
  
  CONSTRAINT pk_res PRIMARY KEY (res_ID)
);

CREATE TABLE ROL_ID(
 rol_ID int NOT NULL UNIQUE,
 rol varchar(20);
  
  CONSTRAINT pk_rol PRIMARY KEY (rol_ID)
);

-- FALTAN------------------

CREATE TABLE PRODUCTO(
 producto_ID SERIAL NOT NULL UNIQUE,
 res_ID varchar(20) NOT NULL,
 corte varchar(20) NOT NULL,
 peso_g float NOT NULL,
 estado varchar(20) NOT NULL,
 comentarios varchar(200),
  
  CONSTRAINT pk_producto PRIMARY KEY (producto_ID)
);

CREATE TABLE TRAZABILIDAD(
 trazabilidad_ID SERIAL NOT NULL UNIQUE,
 res_ID varchar(20) NOT NULL,
 granja boolean,
 matadero boolean,
 planta_desposte boolean,
 
  
  CONSTRAINT pk_trazabilidad PRIMARY KEY (trazabilidad_ID)
);


CREATE TABLE GRANJA(
   rol_ID int,
   trazabilidad_ID SERIAL,
   res_ID varchar(20),
   proveedor_ID varchar(20),
   tempretura_promedio float,
   comentarios varchar(200),
   estado varchar(20),
   fecha_envio date,
   hora_envio date,
  
  CONSTRAINT pk_granja PRIMARY KEY (rol_ID)
);

CREATE TABLE MATADERO(
   rol_ID int,
   trazabilidad_ID SERIAL,
   res_ID varchar(20),
   proveedor_ID varchar(20),
   fecha_recepcion date,
   hora_recepcion date,
   estado_recepcion varchar(20),
   tempretura_promedio float,
   comentarios varchar(200),
   fecha_envio date,
   hora_envio date,
  
  CONSTRAINT pk_matadero PRIMARY KEY (rol_ID),
  CONSTRAINT pk_matadero FOREIGN KEY (rol_ID)
  REFERENCES TRAZABILIDAD(trazabilidad_ID)
);

CREATE TABLE PLANTA_DESPOSTE(
   rol_ID int,
   trazabilidad_ID SERIAL,
   res_ID varchar(20),
   proveedor_ID varchar(20),
   fecha_recepcion date,
   hora_recepcion date,
   estado_recepcion varchar(20),
   tempretura_promedio float,
   comentarios varchar(200),
   fecha_envio date,
   hora_envio date,
  
  CONSTRAINT pk_planta_desposte PRIMARY KEY (rol_ID)
);

CREATE TABLE DISTRIBUIDOR(
   rol_ID int,
   trazabilidad_ID SERIAL,
   res_ID varchar(20),
   proveedor_ID varchar(20),
   fecha_recepcion date,
   hora_recepcion date,
   estado_recepcion varchar(20),
   tempretura_promedio float,
   comentarios varchar(200),
   fecha_venta date,
   hora_venta date,
  
  CONSTRAINT pk_desposte PRIMARY KEY (rol_ID)
);

-- FALTA AGRAGAR LAS RELACIONES --------------
ALTER TABLE PROVEEDOR
ADD CONSTRAINT fk_rol
FOREIGN KEY (rol)
REFERENCES ROL_ID(rol_ID);

ALTER TABLE PRODUCTO
ADD CONSTRAINT fk_res_id
FOREIGN KEY (res_ID)
REFERENCES RES(res_ID);

ALTER TABLE GRANJA
ADD CONSTRAINT fk_trazabilidad
FOREIGN KEY (trazabilidad_ID)
REFERENCES TRAZABILIDAD(trazabilidad_ID);

ALTER TABLE MATADERO
ADD CONSTRAINT fk_trazabilidad
FOREIGN KEY (trazabilidad_ID)
REFERENCES TRAZABILIDAD(trazabilidad_ID);

ALTER TABLE PLANTA_DESPOSTE
ADD CONSTRAINT fk_trazabilidad
FOREIGN KEY (trazabilidad_ID)
REFERENCES TRAZABILIDAD(trazabilidad_ID);

ALTER TABLE DISTRIBUIDOR
ADD CONSTRAINT fk_trazabilidad
FOREIGN KEY (trazabilidad_ID)
REFERENCES TRAZABILIDAD(trazabilidad_ID);

ALTER TABLE table_name
ADD CONSTRAINT fk_foreign_key_name
FOREIGN KEY (foreign_key_name)
REFERENCES target_table(target_key_name);


