from Backend.models.connection_pool import MySQLPool


class TaskModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

################### Users #################################

    # Funcion para agregar un usuario
    def add_user(self, username, password):
        params = {
            'username': username,
            'password': password,
        }
        query = """insert into users (username, password)
            values (%(username)s, %(password)s)"""

        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'iduser': cursor.lastrowid,
                'username': username, 'password': password}

        return data

    # Funcion para obtener un usuario por su ID

    def get_user(self, iduser):
        params = {'iduser': iduser}
        rv = self.mysql_pool.execute(
            "SELECT * from users where iduser=%(iduser)s", params)
        data = []
        content = {}
        for result in rv:
            content = {
                'iduser': result[0], 'username': result[1], 'password': result[2]}
            data.append(content)
            content = {}
        return data

    def get_user_username(self, username):
        params = {'username': username}
        rv = self.mysql_pool.execute(
            "SELECT * from users where username=%(username)s", params)
        content = {}
        for result in rv:
            content = {
                'iduser': result[0], 'username': result[1], 'password': result[2]}
            return content

        return None

    # Funcion para obtener todos los usuarios
    def get_users(self):
        rv = self.mysql_pool.execute("SELECT * from users")
        data = []
        content = {}
        for result in rv:
            content = {
                'iduser': result[0], 'username': result[1], 'password': result[2]}
            data.append(content)
            content = {}
        return data

    # Funcion para eliminar un usuario
    def delete_user(self, iduser):
        params = {'iduser': iduser}
        query = """delete from users where iduser = %(iduser)s"""
        self.mysql_pool.execute(query, params, commit=True)

        data = {'result': 1}
        return data

################### Postulante ################################

    def add_postulant_basic_inf(self, iduser, nombre, apellidoP, apellidoM, dni, correo, celular, ciudad):
        params = {
            'iduser': iduser,
            'nombre': nombre,
            'apellidoP': apellidoP,
            'apellidoM': apellidoM,
            'dni': dni,
            'correo': correo,
            'celular': celular,
            'ciudad': ciudad,
        }
        query = """insert into user_info (iduser, nombre, apellidoP, apellidoM, dni, correo,celular,ciudad)
            values (%(iduser)s, %(nombre)s, %(apellidoP)s, %(apellidoM)s, %(dni)s,%(correo)s,%(celular)s,%(ciudad)s)"""

        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'id': cursor.lastrowid, 'iduser': iduser, 'nombre': nombre, 'apellidoP': apellidoP, 'apellidoM,'
                'dni': dni, 'correo': correo, 'celular': celular, 'ciudad': ciudad}
        return data

    def add_postulant_academic_info(self, id, datePos, curso, estado):
        params = {
            'id': id,
            'datePos': datePos,
            'curso': curso,
            'estado': estado
        }
        query = """insert into profesor(id, datePos,curso,estado) values (%(id)s, %(datePos)s, %(curso)s, %(estado)s)"""
        cursor = self.mysql_pool.execute(query, params, commit=True)
        data = {'id': id, 'datePos': datePos, 'curso': curso, 'estado': estado}
        return data

    # Funcion para obtener un profesor por su ID

    def get_postulant(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute(
            "SELECT * from profesor where id=%(id)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'first_name': result[1], 'dni': result[2],
                       'mail': result[3], 'datef': result[4], 'course': result[5]}
            data.append(content)
            content = {}
        return data

    def get_postulant_username(self, username):
        params = {'username': username}
        rv = self.mysql_pool.execute(
            "SELECT * from users where username=%(username)s", params)
        content = {}
        for result in rv:
            content = {'id': result[0],
                       'username': result[1], 'password': result[2]}
            return content

        return None

    # Funcion para obtener todos los usuarios
    def get_postulants(self):
        # rv = self.mysql_pool.execute("SELECT * from profesor")
        rv = self.mysql_pool.execute(
            'SELECT ui.iduser, CONCAT(ui.nombre," ",ui.apellidoP," ",ui.apellidoM) as Nombre,ui.dni,ui.correo,pr.datePos,pr.curso,pr.estado FROM user_info ui INNER JOIN profesor pr ON ui.iduser = pr.id;')
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'dni': result[2],
                       'mail': result[3], 'datef': result[4], 'course': result[5], 'estado': result[6]}
            data.append(content)
            content = {}
        return data

    # Funcion para eliminar un usuario
    def delete_postulant(self, id):
        params = {'id': id}
        query = """delete from profesor where id = %(id)s"""
        self.mysql_pool.execute(query, params, commit=True)

        data = {'result': 1}
        return data



    def get_estudiante(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from estudiante where id=%(id)s", params)
        return bool(rv)

    def get_profesor(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from profesor where id=%(id)s", params)
        return bool(rv)


################### Administrador ################################

    # Funcion para verificar administrador por su ID

    def get_administrador(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from administrador where id=%(id)s", params)
        return bool(rv)

    # Funcion para obtener datos un administrador por su ID

    def get_administrador_datos(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute(
            "SELECT * from administrador where id=%(id)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los administradores
    def get_administradors(self):
        rv = self.mysql_pool.execute("SELECT * from administrador")
        data = []
        content = {}
        for result in rv:
            content = {'id_adm': result[0], 'rol': result[1]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar un administrador
    def add_administrador(self, rol):
        params = {
            'rol': rol
        }
        query = """insert into administrador (rol)
            values (%(rol)s)"""
        cursor = self.mysql_pool.execute(query, params, commit=True)

        data = {'id_adm': cursor.lastrowid, 'rol': rol}
        return data

    # Funcion para eliminar un administrador
    def delete_administrador(self, id_adm):
        params = {'id_adm': id_adm}
        query = """delete from administrador where id_adm = %(id_adm)s"""
        self.mysql_pool.execute(query, params, commit=True)

        data = {'result': 1}
        return data



################### Actividad ################################
    # Funcion para obtener una actividad por su ID
    def get_actividad(self, id_act):
        params = {'id_act': id_act}
        rv = self.mysql_pool.execute(
            "SELECT * from actividad where id_act=%(id_act)s", params)
        data = []
        content = {}
        for result in rv:
            content = {'id_act': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3],
                       'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todas las actividades
    def get_actividads(self):
        rv = self.mysql_pool.execute("SELECT * from actividad")
        data = []
        content = {}
        for result in rv:
            content = {'id_act': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3],
                       'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar una actividad
    def add_actividad(self, nombre, descripcion, fecha, hora_inicio, hora_fin, estado, enlace_reu):
        params = {
            'nombre': nombre,
            'descripcion': descripcion,
            'fecha': fecha,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin,
            'estado': estado,
            'enlace_reu': enlace_reu
        }
        query = """insert into actividad (nombre, descripcion, fecha, hora_inicio, hora_fin, estado, enlace_reu)
            values (%(nombre)s, %(descripcion)s, %(fecha)s, %(hora_inicio)s, %(hora_fin)s, %(estado)s, %(enlace_reu)s)"""
        cursor = self.mysql_pool.execute(query, params, commit=True)

        data = {'id_act': cursor.lastrowid, 'nombre': nombre, 'descripcion': descripcion, 'fecha': fecha,
                'hora_inicio': hora_inicio, 'hora_fin': hora_fin, 'estado': estado, 'enlace_reu': enlace_reu}
        return data

    # Funcion para eliminar una actividad
    def delete_actividad(self, id_act):
        params = {'id_act': id_act}
        query = """delete from actividad where id_act = %(id_act)s"""
        self.mysql_pool.execute(query, params, commit=True)

        data = {'result': 1}
        return data



if __name__ == "__main__":
    tm = TaskModel()

    # print(tm.create_actividad('prueba 10', 'desde python'))
