# Proyecto final de IS-III - CPTeach

## Trello

 [Enlace](https://trello.com/invite/b/NZPuDOC3/ATTI1e61b3589a3578735cd3740d8cd08937926EEC0C/cpteach-dev-progress)

## Integrantes 
- Alvaro Sergio Cano Luque
- Angie Alexandra Pino Huarsaya
- Fabrizio Miguel Mattos Cahui 
- Gleddynuri Marbel Picha Chañi 
- Joao Franco Emanuel Chávez Salas
- Diego Josue Aquino Quipe
## Contexto
Siempre a comienzos del semestre existen problemas con la asignación de docentes y también para aprender los cursos debidamente, no solo en la universidad sino en el campo educativo, después de la pandemia del 2019 se ha incrementado los problemas de déficit de atención en los estudiantes.
Nuestra preocupacion de esta problematica es grave, porque en la universidad se están perdiendo semanas de clases y para cuando llegue el docente ya no se puede recuperar el tiempo perdido pero de haber usado la aplicación ya se habría avanzado parte del temario del curso y no habría problemas para el examen, desde el punto de vista de los estudiantes este problema se podría resolver con la tecnología que tanto estamos aprendiendo.


## ¿Qué es CPTeach?
CPTeach es una plataforma de administracion y contratacion de docentes, primariamente para el lado universitario. En la cual se recibiran correos con informacion personal en documentos de cada docente el cual desee unirse a la institucion. Ademas de un perfil propio donde se vera salarios, cursos impartidos, tiempo en la institucion, termino de contrato, etc.

## Objetivos

### Objetivo General
Renovar completamente el proceso de eleccion de docentes en la universidad, ademas de poder modularizar el sistema para darle otros usos educativos, como el de admistracion de docentes en general.
### Objetivos Específicos
* *Implementar el uso de automatizacion a la hora de validar titulos profesionales.*
* *Integrar plataformas móviles con plataformas web*
* *Poner en funcionamiento bases de datos y servidores que funcione conjuntamente con la aplicación.*
* *Estudiar el desarrollo de aplicaciones Android y aplicaciones web.*
* *Disminuir la carga laboral del personal docente y administrativo.*
* *Mejorar la administracion y eleccion de docentes*

## Propuesta
Nos proponemos crear una plataforma en donde podamos captar docentes para el dictado de cursos de la carrera, que sigan un proceso de selección y una vez contratados, poder asignarlos a diversos cursos de la carrera. adicionalmente captaremos a docentes que podrán dar sesiones especiales de 1 o 2 horas para reforzar los conocimientos de los alumnos según sea requerido por ellos.
Es posible que se llegue a comercializar porque a pesar de que existen plataformas similares, ésta aplicaría para cursos universitarios en donde hasta ahora no existe una forma de conseguir a un docente por horas adicionales para el reforzamiento del curso según la disposición de tiempo de los estudiantes, ni docentes que puedan cubrirse unos a otros para que se respete el cronograma de clases.
Según los porcentajes en cuanto educación, desde el nivel  inicial hasta el superior, hace falta docentes que refuercen el conocimiento en el nivel primario y superior.
Por lo tanto la razón de la comercialización esta en el porcentaje de estudiantes que no pueden culminar sus estudios universitarios, ya sea por trabajo, problemas familiares entre otros.


## Beneficios
* **Ahorrar tiempo**: Con nuestro sistema tendremos un único punto de referencia para la contratacion de docentes, ademas de poder ser de un lugar administrativo para docentes y secretaria.
* **Aumentar la precisión:** Con el sistema se reduce drásticamente el error humano al revisar documentos ademas de agilizar el proceso de administracion de docentes.
* **Garantizar la integridad de los datos:** En comparación con el antiguo papeleo a la hora de una contratacion y tiempo adicional innecesario, nuestro sistema podra brindar una mayor agilidad a la administracion de la institucion a la cual se le imparta nuestro servicio.
* **Reducir el trabajo administrativo:** La documentacion estara disponible al instante.
* **Disminuir los costes administrativos:** Al poder centralizar diversos sistemas en uno, logramos reducir costos en un alto porcentaje.

## Impacto Social
La iniciativa tiene repercusiones positivas para:
**Estudiantes:** Reducción del el absentismo, mejorar la calidad de las clases impartidas asi generando mejores bases para nuestros futuros profesionales.
**Docentes:** La contratacion es rapida, ademas de evitar perdida de datos.
**Dirección de las Escuelas y Facultades:** El equipo directivo evita mareos a la hora de administrar docentes, al dar notificaciones sobre puntos importantes a la hora del trabajo.

## Diagrama de Clases



## Diagrama de Casos de Uso



## Wireframes
Para las diagramamaciones de las se utilizó Figma


## Funcionalidades

 - [X] Iniciar sesión.
 - [X] Cerrar sesión.
 - [X] Asignar curso a docente.
 - [X] Ver estadísticas de rendimiento de docente (asistencias, faltas, etc).
 - [X] Generar reportes.
 - [X] Editar perfil de docente.
 - [X] Despedir docente.
 - [X] Editar horario.
 - [X] Ver cursos.
 - [X] Ver horarios.
 - [X] Ver salarios.
 - [X] Ver fecha de contratacion/fin de contratacion.

## 📝 Para inicializar el proyecto WEB
Ejecute primero los siguientes comandos en la direccion del proyecto
```
virtualenv env
.\env\Scripts\activate
```
Instalar modulos - SQLite
```
pip install -r requirements.txt
```
Crear Tablas
```
python manage.py makemigrations
$ python manage.py migrate
```
Iniciar la aplicacion
```
python manage.py runserver # default port 8000
```
Iniciar la aplicacion (Puerto modificado)
```
python manage.py runserver 0.0.0.0:<your_port>
```


## Resumen de conceptos utilizados

#### CODIFICACIÓN LEGIBLE (CLEAN CODE)

- Comentarios
- Reglas de nombres
- Consejos de comprensibilidad
- Reglas de funciones
- Objetos y estructuras de datos
- Captalize SQL Special Words


#### PRINCIPIOS SOLID

- Principio de inversión de dependencia (DIP)
- Principio abierto/cerrado (OCP)
- Interface segregation principle(ISP)
- Liskov Substitution Principle (LSP)

#### PRINCIPIOS DE DDD
 - Ubiquitous Lenguage
 - Persistance Ignorance
 - Services

# Conceptos Utilizados

## ESTILOS DE LA PROGRAMACIÓN
- Letterbox
- Tantrum
- Aspects
- Persistent Tables
- Declared Intentions
- Things

### Estilo 1 - Letterbox

#### Descripción
- El problema más grande se descompone en 'cosas' que tienen sentido para el dominio del problema.
- Cada 'cosa' es una cápsula de datos que expone un solo procedimiento, a saber, la capacidad de recibir y enviar mensajes que se le envían.
- El envío de mensajes puede resultar en el envío del mensaje a otra cápsula.

#### Fragmento de código

``` javascript
const express = require("express");
const router = express.Router();
const connectionDb = require("../../config/dbconnections");

class CityModel {
  async getAll() {
    const con = connectionDb.promise();
    const data = await con.query("SELECT * FROM city");
    return data[0];
  }
  async get(id) {
    const con = connectionDb.promise();
    const data = await con.query("SELECT * FROM city WHERE CityID = ?", [id]);
    return data[0];
  }
  async findByName(city) {
    const con = connectionDb.promise();
    const data = await con.query("SELECT * FROM city WHERE City_Name = ?", [
      city,
    ]);
    return data[0];
  }
}
module.exports = CityModel;
```

### Estilo 2 - Tantrum

#### Descripción
- Cada procedimiento y función verifica la cordura de sus argumentos y se niega a continuar cuando los argumentos no son razonables.
- Todos los bloques de código verifican todos los posibles errores, posiblemente imprimen mensajes específicos del contexto cuando ocurren errores y pasan los errores a la cadena de llamadas de función

#### Fragmento de código
``` javascript
const express = require("express");
const router = express.Router();
const VerifyModel = require("../../domain/models/verify.model");
const verifyDb = new VerifyModel();
const CityModel = require("../../domain/models/city.model");
const cityDb = new CityModel();
const CourseModel = require("../../domain/models/course.model");
const SectionModel = require("../../domain/models/section.model");
const sectionDb = new SectionModel();
const TypeModel = require("../../domain/models/type.model");
const typeDb = new TypeModel();
const PersonModel = require("../../domain/models/person.model");
const personDb = new PersonModel();
const courseDb = new CourseModel();

const CourseService = require("../../aplication/services/course.service");
const CourseRepository = require("../../domain/repository/course.repository");

const CityService = require("../../aplication/services/city.service");
const CityRepository = require("../../domain/repository/city.repository");

const TypeService = require("../../aplication/services/type.service");
const TypeRepository = require("../../domain/repository/type.repository");

const SectionService = require("../../aplication/services/type.service");
const SectionRepository = require("../../domain/repository/type.repository");


class DataController {
  constructor() { }
  async getAllPerson() {
    var personRepository = new TypeRepository(personDb);
    var personService = new TypeService(personRepository);
    const result = personService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllVerify() {
    var verifyRepository = new VerifyRepository(personDb);
    var verifyService = new VerifyService(verifyRepository);
    const result = verifyService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllCities() {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const data = await cityService.getAll().catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }


  async getAllType() {
    var typeRepository = new TypeRepository(typeDb);
    var typeService = new TypeService(typeRepository);
    const data = await typeService.getAll().catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllSection() {
    var sectionRepository = new SectionRepository(sectionDb);
    var sectionService = new SectionService(sectionRepository);
    const result = sectionService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCityByName(name) {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const result = cityService.findByName(name);
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCityById(id) {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const result = cityService.get(id);
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllCourses() {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCourseById(id) {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.get(id)
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCourseByName(name) {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.findByName(name)
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }
}
module.exports = DataController;
```

### Estilo 3 - Aspects

#### Descripción
- El problema se descompone utilizando alguna forma de abstracción (procedimientos, funciones, objetos, etc.)
- Los aspectos del problema se agregan al programa principal sin editar el código fuente de las abstracciones. Estas funciones secundarias se aferran a las abstracciones principales nombrándolas, como en "Soy un aspecto de foo (¡aunque puede que foo no lo sepa!)".
#### Fragmento de código
``` javascript
class DataController {
  constructor() { }

  async getAllPerson() {
    var personRepository = new TypeRepository(personDb);
    var personService = new TypeService(personRepository);
    const result = personService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllVerify() {
    var verifyRepository = new VerifyRepository(personDb);
    var verifyService = new VerifyService(verifyRepository);
    const result = verifyService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllCities() {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const data = await cityService.getAll().catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }


  async getAllType() {
    var typeRepository = new TypeRepository(typeDb);
    var typeService = new TypeService(typeRepository);
    const data = await typeService.getAll().catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllSection() {
    var sectionRepository = new SectionRepository(sectionDb);
    var sectionService = new SectionService(sectionRepository);
    const result = sectionService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCityByName(name) {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const result = cityService.findByName(name);
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCityById(id) {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const result = cityService.get(id);
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllCourses() {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCourseById(id) {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.get(id)
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCourseByName(name) {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.findByName(name)
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }
}

module.exports = DataController;
```

Uso de clases y funciones referente

``` javascript
const BaseRepository = require("./base.repository");

class CityRepository extends BaseRepository {
  constructor(CityDb) {
    super(CityDb);
  }

  async getAllWithoutPagination() {
    return this.model.find();
  }
}

module.exports = CityRepository;
```

### Estilo 4 Persistent Tables

#### Descripción

- Los datos de entrada del problema se modelan como entidades con relaciones entre ellas

- Los datos se colocan en tablas, con columnas que potencialmente hacen referencia cruzada a datos en otras tablas

- Existencia de un motor de consulta relacional

- El problema se resuelve emitiendo consultas sobre los datos tabulares.

#### Fragmento de código

```javascript
async findByName(city) {
  const con = connectionDb.promise();
  const data = await con.query("SELECT * FROM city WHERE City_Name = ?", [
    city,
  ]);
  return data[0];
}
async getAll() {
  const connection = connectionDb.promise();
  const data = await con.query(
    "SELECT * FROM student INNER JOIN person ON student.PersonID = person.PersonID INNER JOIN city ON person.CityID = city.CityID"
  );
  return data[0];
}
```

### Estilo 5 Declared Intentions

#### Descripción

- Existencia de un verificador de tipos en tiempo de ejecución

- Los procedimientos y funciones declaran qué tipos de argumentos esperan

- Si las personas que llaman envían argumentos de tipos que no se esperan, el
   los procedimientos/funciones no se ejecutan.
  
#### Fragmento de código
 
```javascript
  async deleteInscription(id, StudentId) {
    if (!id || !StudentId) {
      const error = new Error();
      error.status = 100;
      error.message = "El parámetro ID debe ser enviado";
      throw error;
    }
    const entity = await this.repository.deleteInscription(id, StudentId);
    if (!entity) {
      const error = new Error();
      error.status = 500;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }
```

### Estilo 6 Things

#### Descripción

- El problema mayor se descompone en 'cosas' que tienen sentido para el dominio del problema.
- Cada 'cosa' es una cápsula de datos que expone procedimientos al resto del mundo.
- Nunca se accede a los datos directamente, solo a través de estos procedimientos.
- Las cápsulas pueden reapropiarse de procedimientos definidos en otras cápsulas.

#### Fragmento de código
```javascript
class BaseRepository {
  constructor(model) {
    this.model = model;
  }
  async get(id) {
    return this.model.get(id);
  }
  async getAll() {
    return this.model.getAll();
  }
  async getByName(name) {
    return this.model.getByName(name);
  }
  async create(entity) {
    return this.model.create(entity);
  }
  async update(entity) {
    return this.model.update(entity);
  }
  async delete(id) {
    return this.model.delete(id);
  }
}
```

### Clean Code 1 - Comentarios

#### Descripción

- Intenta siempre explicarte en código.
- No seas redundante.
- No agregue ruido obvio.
- No use comentarios de llaves de cierre.
- No comente el código. Solo elimina.
- Utilizar como explicación de la intención. 
- Utilizar como aclaración de código.
- Utilizar como advertencia de las consecuencias.

#### Framgmento de código

Uso de comentarios respetando las reglas designadas 

``` javascript
const express = require("express");
const router = express.Router();
const PersonModel = require("../../domain/models/person.model");
const personDb = new PersonModel();
const LoginModel = require("../../domain/models/login.model");
const loginDb = new LoginModel();
const ProfessorModel = require("../../domain/models/professor.model");
const professorDb = new ProfessorModel();
const InscriptionModel = require("../../domain/models/inscription.model");
const inscriptionDb = new InscriptionModel();
const CourseModel = require("../../domain/models/course.model")
const courseDb = new CourseModel();
const CourseStudentsModel = require("../../domain/models/course_student.model");
const courseStudentsDb = new CourseStudentsModel();
const SheduleModel = require("../../domain/models/shedule.model");
const sheduleDb = new SheduleModel();

// Instancias requeridas
const ProfessorService = require("../../aplication/services/professor.service");
const ProfessorRepository = require("../../domain/repository/professor.repository");

const InscriptionService = require("../../aplication/services/inscription.service");
const InscriptionRepository = require("../../domain/repository/inscription.repository");

const SheduleService = require("../../aplication/services/shedule.service");
const SheduleRepository = require("../../domain/repository/shedule.repository");

const CourseService = require("../../aplication/services/course.service");
const CourseRepository = require("../../domain/repository/course.repository");

const PersonService = require("../../aplication/services/person.service");
const PersonRepository = require("../../domain/repository/person.repository");

const LoginService = require("../../aplication/services/login.service");
const LoginRepository = require("../../domain/repository/login.repository");

const CourseStudentsService = require("../../aplication/services/courseStudents.service");
const CourseStudentsRepository = require("../../domain/repository/courseStudents.repository");


// Definicion de funciones
class ProfessorController {
  //Obtiene todos los profesores
  async getAll() {
    var professorRepository = new ProfessorRepository(professorDb);
    var professorService = new ProfessorService(professorRepository);
    const result = profesorService.getAll()
    const data = await result.catch((err) => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }
  
  //Busca profesor por su codigo 
  async findBydCode(code) {
    var professorRepository = new ProfessorRepository(professorDb);
    var professorService = new ProfessorService(professorRepository);
    const result = professorService.findBydCode(code)
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }
  
  //vincula curso con estudiante
  async studentInscription(StudentID, CourseID) {
    var inscriptionRepository = new InscriptionRepository(inscriptionDb);
    var inscriptionService = new InscriptionService(inscriptionRepository);
    const result = inscriptionService.create({ StudentID, CourseID });
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }
 
  //Crea un nuevo horario
  async NuevoHorario(Day, Start, Finish, CourseID) {
    var sheduleRepository = new SheduleRepository(sheduleDb);
    var sheduleService = new SheduleService(sheduleRepository);
    const result = sheduleService.create({ Day, Start, Finish, CourseID });
    const data = await result.catch((err) => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }
 
 //se obtiene el horario
  async GetHorario(CourseID) {
    var sheduleRepository = new SheduleRepository(sheduleDb);
    var sheduleService = new SheduleService(sheduleRepository);
    const result = sheduleService.get(CourseID);
    const data = await result.catch((err) => {
      console.log("controller Error Get Horario ", err);
      return null;
    });
    return data;
  }
  
  //se crea un nuevo curso
  async NuevoCourse(Course_Name, SectionID, TypeID, ProfessorID, NumEst, Semestre) {
    var courseRepository = new CourseRepository(courseDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.create({ Course_Name, SectionID, TypeID, ProfessorID, NumEst, Semestre });
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });

    return data;
  }

  async register(
    First_Name,
    Last_Name,
    Email,
    DNI,
    Mobile_Phone,
    CityID,
    Department,
    Password,
    idDNI) {
    var personRepository = new PersonRepository(personDb);
    var personService = new PersonService(personRepository);
    var professorRepository = new ProfessorRepository(professorDb);
    var professorService = new ProfessorService(professorRepository);
    var loginRepository = new LoginRepository(loginDb);
    var loginService = new LoginService(loginRepository);

    const result = personService.create(

      First_Name,
      Last_Name,
      Email,
      DNI,
      null,
      Mobile_Phone,
      CityID

    );

    const data = await result.catch((err) => {
      console.log("controller Error", err);
      return null;
    });

    let dataId;
    const resultProfessor = professorService.create({ Department, dataId, idDNI });
    const dataProfessor = await resultProfessor.catch(err => {
      console.log("controller Error Professor", err);
      return null;
    })

    let val = null;
    let rol = 1;
    const resultLogin = loginService.create({ Email, Password, val, idDNI, rol });
    const dataLogin = await result.catch((err) => {
      console.log("controller Error", err);
      return null;
    });
    console.log("dataLogin", dataLogin);
    return dataLogin;
  }

  async login(email, password) {
    var loginRepository = new LoginRepository(loginDb);
    var loginService = new LoginService(loginRepository);
    const resulLogin = loginService.authenticate(email, password);
    const dataLogin = await resulLogin.catch((err) => {
      console.log("controller Error", err);
      return null;
    });
    return dataLogin;
  }

  async getAllCourses(id) {
    var courseRepository = new CourseRepository(courseDb);
    var courseService = new CourseService(courseRepository);

    const resultCourse = await courseService.findByIdProfessor(id)
      .catch((err) => {
        console.log("Controller Error", err);
        return null;
      });
    return resultCourse;
  }


  async getProfessorToCourse(token) {
    var professorRepository = new ProfessorRepository(professorDb);
    var professorService = new ProfessorService(professorRepository);

    const resultProfessor = professorService.findByDNI(token);
    const dataProfessor = await resultProfessor.catch((err) => {
      console.log("Controller error", err);
      return null;
    });
    return dataProfessor;
  }

  async getStudentsOfCourses(token) {
    var courseStudentsRepository = new CourseStudentsRepository(courseStudentsDb);
    var courseStudentsService = new CourseStudentsService(courseStudentsRepository);

    const resultStudentsCourse = courseStudentsService.studentsForCourse(token);
    const dataStudentsCourse = await resultStudentsCourse.catch((err) => {
      console.log("Controller error", err);
      return null;
    });
    return dataStudentsCourse;
  }

  async deleteCourse(id) {
    var courseRepository = new CourseRepository(courseDb);
    var courseService = new CourseService(courseRepository);

    const result = courseService.delete(id);
    const data = await result.catch((err) => {
      console.log("Controller error", err);
      return null;
    });
    return data;
  }

  async getCourse(id) {
    var courseRepository = new CourseRepository(courseDb);
    var courseService = new CourseService(courseRepository);

    const result = courseService.get(id)
    const data = await result.catch((err) => {
      console.log("Controller error", err);
      return null;
    });
    return data;
  }

  async updateCourse(name, section, type, semestre, id) {
    var courseRepository = new CourseRepository(courseDb);
    var courseService = new CourseService(courseRepository);

    const result = courseService.update({ name, section, type, semestre, id })
    const data = await result.catch((err) => {
      console.log("Controller error", err);
      return null;
    });
    return data;
  }

}

module.exports = ProfessorController;
```

### Clean Code 2 - Reglas de nombres

- Elija nombres descriptivos e inequívocos.
- Hacer una distinción significativa.
- Usa nombres pronunciables.
- Utilice nombres buscables.
- Reemplace los números mágicos con constantes con nombre.
- Evite las codificaciones. No agregue prefijos ni escriba información.


#### Fragmento de código

Respetando las reglas de nombre , podemos observar en la sigueinte imagen que el nombre de las funciones como el de las variables no son ambiguas , y son muy descriotivas , encontradas en el dataController para más informacion.

``` javascript

class DataController {
  constructor() { }

  async getAllPerson() {
    var personRepository = new TypeRepository(personDb);
    var personService = new TypeService(personRepository);
    const result = personService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllVerify() {
    var verifyRepository = new VerifyRepository(personDb);
    var verifyService = new VerifyService(verifyRepository);
    const result = verifyService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllCities() {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const data = await cityService.getAll().catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }


  async getAllType() {
    var typeRepository = new TypeRepository(typeDb);
    var typeService = new TypeService(typeRepository);
    const data = await typeService.getAll().catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllSection() {
    var sectionRepository = new SectionRepository(sectionDb);
    var sectionService = new SectionService(sectionRepository);
    const result = sectionService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCityByName(name) {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const result = cityService.findByName(name);
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCityById(id) {
    var cityRepository = new CityRepository(cityDb);
    var cityService = new CityService(cityRepository);
    const result = cityService.get(id);
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async getAllCourses() {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.getAll();
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCourseById(id) {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.get(id)
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }

  async findCourseByName(name) {
    var courseRepository = new CourseRepository(CoursesDb);
    var courseService = new CourseService(courseRepository);
    const result = courseService.findByName(name)
    const data = await result.catch(err => {
      console.log("controller Error", err);
      return null;
    });
    return data;
  }
}

module.exports = DataController;
```

### Clean Code 3 - Consejos de comprensibilidad

#### Despcripción 
- Se consistente. Si haces algo de cierta manera, haz todas las cosas similares de la misma manera.
- Usa variables explicativas.
- Encapsular las condiciones de contorno. Las condiciones de contorno son difíciles de seguir. Ponga el procesamiento para ellos en un solo lugar.
- Prefiere los objetos de valor dedicados al tipo primitivo.
- Evita la dependencia lógica.
- No escriba métodos que funcionen correctamente dependiendo de otra cosa en la misma clase.
- Evita los condicionales negativos.

#### Fragmento de Código
Uso de variables de entorno uso del código

``` javascript
require("dotenv").config();
const mysql = require("mysql2");
// create the pool
const pool = mysql.createPool({
  host: process.env.HOST,
  user: process.env.USER,
  database: process.env.DATABASE,
  password: process.env.PASSWORD,
});

module.exports = pool;
```

### Clean Code 4 - Reglas de funciones
#### Descripción
- Pequeña.
- Haz una cosa.
- Utilice nombres descriptivos.
- Prefiere menos argumentos.
- No tiene efectos secundarios.
- No use argumentos de bandera. Divida el método en varios métodos independientes que se pueden llamar desde el cliente sin la bandera.

#### Fragmento de Código
_1 El nombre de las funciones son descriptivas , además en todas las funciones realizadas los parametros no exceden de 7 parámetros referente en el código en [Click aqui](https://github.com/VILLA7523/FinalProjectIS/blob/main/Application/src/domain/repository/base.repository.js)_

``` javascript
class BaseRepository {
  constructor(model) {
    this.model = model;
  }
  async get(id) {
    return await this.model.get(id);
  }
  async getAll() {
    return await this.model.getAll();
  }
  async getByName(name) {
    return await this.model.getByName(name);
  }
  async create(entity) {
    return await this.model.create(entity);
  }
  async update(entity) {
    return await this.model.update(entity);
  }
  async delete(id) {
    return await this.model.delete(id);
  }
}
module.exports = BaseRepository;
```

### Clean Code 5 - Objetos y estructuras de datos
#### Descripción
- Ocultar estructura interna.
- Preferir estructuras de datos.
- Evita estructuras híbridas (mitad objeto y mitad datos).
- Debería ser pequeño.
- Haz una cosa.
- Pequeño número de variables de instancia.
- La clase base no debe saber nada acerca de sus derivados.
- Es mejor tener muchas funciones que pasar algo de código a una función para seleccionar un comportamiento.
- Prefiere métodos no estáticos a métodos estáticos.

### Fragmento de código

``` javascript
const BaseService = require("./base.service");

class CourseService extends BaseService {
  constructor(CourseRepository) {
    super(CourseRepository);
    this._CourseRepository = CourseRepository;
  }

  async findByIdProfessor(id) {
    if (!id) {
      const error = new Error();
      error.status = 400;
      error.message = "Email or password missing";
      throw error;
    }

    const entity = await this.repository.findByIdProfessor(id);

    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Failed authentication";
      throw error;
    }
    return entity;
  }
  //si es true aumenta , si es fals disminuye

  async updateCantEstIn(id) {
    if (!id) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro id debe ser enviado";
      throw error;
    }

    const entity = await this.repository.updateCantEstIn(id);

    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async updateCantEstDe(id) {
    if (!id) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro id debe ser enviado";
      throw error;
    }

    const entity = await this.repository.updateCantEstDe(id);

    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }
}

module.exports = CourseService;
```

``` javascript
const BaseRepository = require("./base.repository");

class CourseRepository extends BaseRepository {
  constructor(CourseDb) {
    super(CourseDb);
  }
  async findByIdProfessor(id) {
    return await this.model.findByIdProfessor(id);
  }
}

module.exports = CourseRepository
```

``` javascript
  async getCourse(id) {
    var courseRepository = new CourseRepository(courseDb);
    var courseService = new CourseService(courseRepository);

    const result = courseService.get(id)
    const data = await result.catch((err) => {
      console.log("Controller error", err);
      return null;
    });
    return data;
  }

  async updateCourse(name, section, type, semestre, id) {
    var courseRepository = new CourseRepository(courseDb);
    var courseService = new CourseService(courseRepository);

    const result = courseService.update({ name, section, type, semestre, id })
    const data = await result.catch((err) => {
      console.log("Controller error", err);
      return null;
    });
    return data;
  }
```

### Clean Code - 6 Capitalize SQL Special Words
#### Descripción
- La interacción con la base de datos es una parte importante de la mayoría de las aplicaciones web. Si está escribiendo consultas SQL sin procesar, es una buena idea mantenerlas legibles también.
- Aunque las palabras especiales de SQL y los nombres de funciones no distinguen entre mayúsculas y minúsculas, es una práctica común usar mayúsculas para distinguirlos de los nombres de tablas y columnas.

Fragmento de Código

```
const express = require("express");
const router = express.Router();
const connectionDb = require("../../config/dbconnections");

class CurseAttendanceModel {
  async create({ AttendanceId, StudentID, ProfessorID, CourseID }) {
    const con = connectionDb.promise();
    const data = await con.query(
      "INSERT INTO curse_attendances (AttendanceId,StudentID,ProfessorID,CourseID) VALUES (?,?,?,?)",
      [AttendanceId, StudentID, ProfessorID, CourseID]
    );
    return data[0];
  }
}
module.exports = CurseAttendanceModel;
```
## PRINCIPIOS SOLID

- Principio de inversión de dependencia (DIP)
- Principio abierto/cerrado (OCP)
- Interface segregation principle(ISP)
- Liskov Substitution Principle (LSP)

### 1-  Principio de inversión de dependencia (DIP)

#### Descripción
Este principio establece dos cosas esenciales:

- Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deberían depender de abstracciones.
- Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.
Esto puede ser difícil de entender al principio,
pero si has trabajado con marcos PHP (como Symfony), has visto una implementación de este principio en forma de inyección de dependencia (DI). Si bien no son conceptos idénticos, DIP evita que los módulos de alto nivel conozcan los detalles de sus módulos de bajo nivel y los configuren. Puede lograr esto a través de DI.
Un gran beneficio de esto es que reduce el acoplamiento entre módulos. El acoplamiento es un patrón de desarrollo muy malo porque hace que su código sea difícil de refactorizar.

#### Fragmento de código
En nuestra implementación se cumple este principio , un ejemplo de ello son en lo servicios , repository , etc . todas las funciones que se usaran en el proyecto son propias de cada modelo esto quiere decir , que en cada clase se impletan funciones que no comparte con las demás , y las que si son genéricas se establecen en una clase base , tomando en cuenta las principales funciones crud asi como los filtros.

Implementacion de baseService , se puede observar las principales funciones crud.

``` javascript
class BaseService {
  constructor(Repository) {
    this.repository = Repository;
  }
  async get(id) {
    if (!id) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro id debe ser enviado";
      throw error;
    }

    const entity = await this.repository.get(id);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async getByName(name) {
    if (!name) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro name debe ser enviado";
      throw error;
    }

    const entity = await this.repository.getByName(name);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async getAll() {
    const entity = await this.repository.getAll();
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async create(data) {
    const entity = await this.repository.create(data);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async update(data) {
    const entity = await this.repository.update(data);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async delete(id) {
    const entity = await this.repository.delete(id);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }
}
```

De esta clase base extienden otras como: 

CouserStudetsService , se observa que solo esta implementado funciones propias de esta.

```javascript
const BaseService = require("./base.service");

class CourseStudentsService extends BaseService {
  constructor(CourseStudentsRepository) {
    super(CourseStudentsRepository);
    this._CourseStudentsRepository = CourseStudentsRepository;
  }
  async studentsForCourse(token) {
    if (!token) {
      const error = new Error();
      error.status = 400;
      error.message = "token parameter is missing";
      throw error;
    }

    const entity = await this.repository.studentsForCourse(token);

    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Student not found";
      throw error;
    }
    return entity;
  }
}

module.exports = CourseStudentsService;
```

LoginService , se observa que solo esta implementado funciones propias de esta.

``` javascript
const BaseService = require("./base.service");

class LoginService extends BaseService {
  constructor(LoginRepository) {
    super(LoginRepository);
    this._LoginRepository = LoginRepository;
  }

  async authenticate(email, password) {
    if (!email || !password) {
      const error = new Error();
      error.status = 400;
      error.message = "Email or password missing";
      throw error;
    }

    const entity = await this.repository.authenticate(email, password);

    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Failed authentication";
      throw error;
    }
    return entity;
  }
}

module.exports = LoginService;
```

### 2 - Principio abierto/cerrado (OCP)
#### Descripción
El Principio Abierto/Cerrado, también conocido como Open/Closed Principle o por sus siglas OCP, es el segundo de los 5 principios SOLID de la programación orientada a objetos.

Los módulos que cumplen con el principio abierto-cerrado tienen dos características principales. Estos son

 - Abiertos para la extensión: Esto significa que el comportamiento del módulo puede ser extendido. Cuando los requerimientos de la aplicación cambian, debemos ser capaces de extender el módulo con estos nuevos comportamientos que satisfagan esos cambios. En otras palabras, debemos ser capaces de cambiar lo que el módulo hace.
 - Cerrado para la modificación: Esto significa que extender el comportamiento de un módulo no debería tener como resultado cambiar el código fuente, es decir, el código original debe permanecer sin cambios.

#### Fragmento de Código
La siguiente fragmento de código muestra la implementación de la clase BaseRepository , en la cual se encuentran las funciones crud , cumple con las caracteristica de este principio ya que se puede observar que en la clase baseRepository estan implementadas las funciones crud , que todos nuestros modelos usaran , de esta clase ectendimos más clases en las cuales hay funciones propias de cada repositorio:

En el siguiente fragmento de código podemos observar que los parámetros de las funciones , reciben un objeto , esto con el objetivo de hacer que las funciones sean génericas y cualquier repository que estiendan a ella sean independientes a sus parámetros 

``` Javascript
class BaseRepository {
  constructor(model) {
    this.model = model;
  }
  async get(id) {
    return this.model.get(id);
  }
  async getAll() {
    return this.model.getAll();
  }
  async getByName(name) {
    return this.model.getByName(name);
  }
  async create(entity) {
    return this.model.create(entity);
  }
  async update(entity) {
    return this.model.update(entity);
  }
  async delete(id) {
    return this.model.delete(id);
  }
}
```

En las siguientes imagenes son nuestras implementaciones .repository que extienden del baseRepository:

implementación de loginRepository , como se observa authenticate es propio de login , pues ninguna de las otras clases lo comparte , es por eso que est funcionalidad se desarrolla dentro de la clase porpia de esta 

``` javascript
const BaseRepository = require("./base.repository");

class LoginRepository extends BaseRepository {
  constructor(LoginDb) {
    super(LoginDb);
  }

  async authenticate(email , password) {
    return await this.model.authenticate(email , password);
  }
}

module.exports = LoginRepository
```

Implementación de courseStudentsRepository que extiende de BaseRepository 

``` javascript
const BaseRepository = require("./base.repository");

class CourseStudentsRepository extends BaseRepository {
  constructor(CourseStudentsDb) {
    super(CourseStudentsDb);
  }
  async studentsForCourse(token) {
    return await this.model.studentsForCourse(token);
  }
}

module.exports = CourseStudentsRepository
```

Implementación de Course que extiende de baseRepository

const BaseRepository = require("./base.repository");

``` javascript
class CourseRepository extends BaseRepository {
  constructor(CourseDb) {
    super(CourseDb);
  }

  async getAllWithoutPagination() {
    return await this.model.find();
  }

  async findByIdProfessor(id) {
    return await this.model.findByIdProfessor(id);
  }
}

module.exports = CourseRepository
```


### 3 - Interface segregation principle(ISP)

#### Descripción
- No se debe obligar a los clientes a depender de métodos que no utilizan. Cuando se requiere que una Clase realice acciones que no son útiles, es un desperdicio y puede producir errores inesperados si la Clase no tiene la capacidad de realizar esas acciones.
- Una clase debe realizar solo las acciones necesarias para cumplir su función. Cualquier otra acción debe eliminarse por completo o moverse a otro lugar si otra Clase podría usarla en el futuro.

#### Fragmento de Código
Los metodos principales usados para el CRUD estan definidos tanto en base.repository.js como en base.service.js respectivamente , aqui cumplimos con lo mecionado anteriormente , de que no se debe colocar funcionalidades que no usemos , es por ello que estas clases definen solo acciones que otra clases podría cumplir en un futuro , y en general las que toda clase debe usar.  

Implementación de base repository , asi mismo esta clase funciona como interfaz entre los mmodels y los services

``` Javascript
class BaseRepository {
  constructor(model) {
    this.model = model;
  }
  async get(id) {
    return this.model.get(id);
  }
  async getAll() {
    return this.model.getAll();
  }
  async getByName(name) {
    return this.model.getByName(name);
  }
  async create(entity) {
    return this.model.create(entity);
  }
  async update(entity) {
    return this.model.update(entity);
  }
  async delete(id) {
    return this.model.delete(id);
  }
}
```

Implementación de Base Service , asi mismo esta clase funciona como interfaz entre los controllers y los repository

``` javascript
class BaseService {
  constructor(Repository) {
    this.repository = Repository;
  }
  async get(id) {
    if (!id) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro id debe ser enviado";
      throw error;
    }

    const entity = await this.repository.get(id);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async getByName(name) {
    if (!name) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro name debe ser enviado";
      throw error;
    }

    const entity = await this.repository.getByName(name);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async getAll() {
    const entity = await this.repository.getAll();
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async create(data) {
    const entity = await this.repository.create(data);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async update(data) {
    const entity = await this.repository.update(data);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async delete(id) {
    const entity = await this.repository.delete(id);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }
}
```

### 4 - Liskov Substitution Principle

#### Descripción

Cuando una Clase hija no puede realizar las mismas acciones que su Clase padre, esto puede causar errores.

Si tienes una clase y creas otra clase a partir de ella, ésta se convierte en padre y la nueva clase en hijo. La clase hija debe ser capaz de hacer todo lo que la clase padre puede hacer. Este proceso se llama Herencia.

La clase hija debe ser capaz de procesar las mismas peticiones y entregar el mismo resultado que la clase padre o puede entregar un resultado que sea del mismo tipo.

La imagen muestra que la clase padre entrega café (puede ser cualquier tipo de café). Es aceptable que la Clase hija entregue Cappucino porque es un tipo específico de Café, pero NO es aceptable que entregue Agua.

Si la Clase hija no cumple con estos requisitos, significa que la Clase hija ha cambiado completamente y viola este principio.

#### Objetivo

Este principio tiene como objetivo reforzar la consistencia para que la Clase padre o su Clase hija puedan ser utilizadas de la misma manera sin ningún error.

#### Fragmento de código

```javascript
// PARENT

class BaseService {
  constructor(Repository) {
    this.repository = Repository;
  }
  async get(id) {
    if (!id) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro id debe ser enviado";
      throw error;
    }

    const entity = await this.repository.get(id);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async getByName(name) {
    if (!name) {
      const error = new Error();
      error.status = 400;
      error.message = "Parametro name debe ser enviado";
      throw error;
    }

    const entity = await this.repository.getByName(name);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async getAll() {
    const entity = await this.repository.getAll();
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async create(data) {
    const entity = await this.repository.create(data);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async update(data) {
    const entity = await this.repository.update(data);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }

  async delete(id) {
    const entity = await this.repository.delete(id);
    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Entidad no encontrada";
      throw error;
    }
    return entity;
  }
}

module.exports = BaseService;

// CHILD

const BaseService = require("./base.service");

class CityService extends BaseService {
  constructor(CityRepository) {
    super(CityRepository);
    this._cityRepository = CityRepository;
  }
}

module.exports = CityService;

 ```
 
 ## PRINCIPIOS DE DDD
 - Ubiquitous Lenguage
 - Persistance Ignorance
 - Services
 
 ### 1 - Ubiquitous Lenguage
 
 #### Descripción 
- El lenguaje ubicuo debe expresarse en el modelo de dominio.
- Ubiquitous Language une a las personas del equipo del proyecto.
- Ubiquitous Language elimina imprecisiones y contradicciones de los expertos del dominio.
- El lenguaje ubicuo no es un lenguaje de negocios impuesto por expertos en dominios.
- El lenguaje ubicuo no es un lenguaje utilizado en las industrias.
- El lenguaje ubicuo evoluciona con el tiempo, no se define por completo en una sola reunión.
- Los conceptos que no forman parte del Lenguaje Ubicuo deben ser rechazados.

 #### Fragmento de código
 
 En todo el código desarrollado seguimos buenas practicas y además considerando un lenguaje común para todo el desarrollo final.
 
 ```javascript
 const BaseRepository = require("./base.repository");

class LoginRepository extends BaseRepository {
  constructor(LoginDb) {
    super(LoginDb);
  }
  async getAllWithoutPagination() {
    return this.model.find();
  }

  async authenticate(email, password) {
    return this.model.authenticate(email, password);
  }
}

module.exports = LoginRepository;
 ```
 
 ### 2 - Persistance Ignorance
 
 #### Descripción 
 - Dentro de DDD no se graba se persiste
 - La utilización de la información que provee el modelo esta desligada de la forma de presentación.
 
 #### Fragmento de código
 
 Al utilizar las tablas de persistencia, podemos ver que seguimos el principio de persistencia, ademas que las funciones desarrolladas en el modelo estan completamente desligadas del uso que se le dé posteriormente.
 
 ```javascript
 const express = require("express");
const router = express.Router();
const connectionDb = require("../../config/dbconnections");

class PersonModel {
  async getAll() {
    const con = connectionDb.promise();
    const data = await con.query("SELECT * FROM person");
    return data[0];
  }
  async create({ First_Name, Last_Name, Email, DNI, Mobile_Phone, CityID }) {
    const con = connectionDb.promise();
    const data = await con.query(
      "INSERT INTO person (First_Name,Last_Name,Email,DNI,Home_Phone,Mobile_Phone,CityID) VALUES (?,?,?,?,?,?,?)",
      [First_Name, Last_Name, Email, DNI, null, Mobile_Phone, CityID]
    );
    return data[0].insertId;
  }
}
module.exports = PersonModel;
 ```
 
 ### 3 - Services
 #### Descripción 
 - Los servicios de la aplicación son la interfaz utilizada por el mundo exterior, donde el mundo exterior no puede comunicarse a través de nuestros objetos Entidad.
 - La intefaz puede obtener representaciones no directas de ellos. 
 - Los Servicios de aplicaciones asignan mensajes externos a operaciones y procesos internos
 - Los servicios se encargan de la comunicación entre las capas de Dominio e Infraestructura para proporcionar operaciones cohesivas para clientes externos.

#### Fragmento de código
Aqui podemos observar como un servicio se comunica con los repositorios conectando de esta forma las capas.

 ```javascript
 const BaseService = require("./base.service");

class LoginService extends BaseService {
  constructor(LoginRepository) {
    super(LoginRepository);
    this._LoginRepository = LoginRepository;
  }

  async authenticate(email, password) {
    if (!email || !password) {
      const error = new Error();
      error.status = 400;
      error.message = "Email or password missing";
      throw error;
    }

    const entity = await this.repository.authenticate(email, password);

    if (!entity) {
      const error = new Error();
      error.status = 400;
      error.message = "Failed authentication";
      throw error;
    }
    return entity;
  }
}

module.exports = LoginService;
 ```

