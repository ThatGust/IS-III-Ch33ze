CREATE DATABASE cpteach_isiii;
USE cpteach_isiii;
CREATE TABLE users(
	iduser INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(15),
    password VARCHAR(30)
);
CREATE TABLE user_info(
	iduser_info INTEGER NOT NULL AUTO_INCREMENT,
    iduser INTEGER NOT NULL,
    nombre VARCHAR(10),
    apellidoP VARCHAR(10),
    apellidoM VARCHAR(10),
    dni VARCHAR(20),
    correo VARCHAR(50),
    celular VARCHAR(20),
    ciudad VARCHAR(15),
    PRIMARY KEY(iduser_info,iduser)
);
CREATE TABLE estudiante(
	id INTEGER NOT NULL PRIMARY KEY,
    carrera VARCHAR(30)
);

CREATE TABLE profesor(
	id INTEGER NOT NULL PRIMARY KEY,
    foto VARCHAR(255),
    datePos varchar(40),
    curso VARCHAR(60),
    curriculum VARCHAR(255),
    -- departamento VARCHAR(35),
    estado VARCHAR(10)
);

CREATE TABLE administrador(
	id INTEGER NOT NULL PRIMARY KEY
);

CREATE TABLE curso(
	id_curso INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(60),
    descripcion TEXT,
    silabo VARCHAR(50),
    n_alumnos INTEGER
);

CREATE TABLE horario(
	id_schedule INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    hora_inicio VARCHAR(30),
    hora_final VARCHAR(30)
);

CREATE TABLE administrador_profesor(
	id_profesor INTEGER NOT NULL,
    id_administrador INTEGER NOT NULL,
    PRIMARY KEY(id_profesor,id_administrador)
);
CREATE TABLE estudiante_curso(
	id INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    PRIMARY KEY(id,id_curso)
);

CREATE TABLE profesor_curso(
	id INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    PRIMARY KEY(id,id_curso)
);

CREATE TABLE schedule_curso(
	id_curso INTEGER NOT NULL,
    id_schedule INTEGER NOT NULL,
    PRIMARY KEY(id_curso, id_schedule)
);
ALTER TABLE estudiante ADD FOREIGN KEY (id) REFERENCES users(iduser);
ALTER TABLE profesor ADD FOREIGN KEY (id) REFERENCES users(iduser);
ALTER TABLE administrador ADD FOREIGN KEY (id) REFERENCES users(iduser);
ALTER TABLE user_info ADD FOREIGN KEY (iduser) REFERENCES users(iduser);
ALTER TABLE administrador_profesor ADD FOREIGN KEY (id_profesor) REFERENCES profesor(id);
ALTER TABLE administrador_profesor ADD FOREIGN KEY (id_administrador) REFERENCES administrador(id);
ALTER TABLE estudiante_curso ADD FOREIGN KEY (id) REFERENCES estudiante(id);
ALTER TABLE estudiante_curso ADD FOREIGN KEY (id_curso) REFERENCES curso(id_curso);
ALTER TABLE profesor_curso ADD FOREIGN KEY (id) REFERENCES profesor(id);
ALTER TABLE profesor_curso ADD FOREIGN KEY (id_curso) REFERENCES curso(id_curso);
ALTER TABLE schedule_curso ADD FOREIGN KEY (id_curso) REFERENCES curso(id_curso);
ALTER TABLE schedule_curso ADD FOREIGN KEY (id_schedule) REFERENCES horario(id_schedule);