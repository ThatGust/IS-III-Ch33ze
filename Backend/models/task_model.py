from Backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

################### Users #################################

    # Funcion para agregar un usuario
    def add_user(self, username, password):
        params = {
            'username' : username,
            'password' : password,
        }
        query = """insert into user (username, password)
            values (%(username)s, %(password)s)"""
         
        cursor = self.mysql_pool.execute(query, params, commit=True)   
        data = {'iduser': cursor.lastrowid, 'username': username, 'password': password}

        return data

    # Funcion para obtener un usuario por su ID

    def get_user(self, iduser):
        params = {'iduser' : iduser}      
        rv = self.mysql_pool.execute("SELECT * from user where iduser=%(iduser)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'iduser': result[0], 'username': result[1], 'password': result[2]}
            data.append(content)
            content = {}
        return data

    def get_user_username(self, username):
        params = {'username' : username}      
        rv = self.mysql_pool.execute("SELECT * from user where username=%(username)s", params)                
        content = {}
        for result in rv:
            content = {'iduser': result[0], 'username': result[1], 'password': result[2]}
            return content
        
        return None
            

    # Funcion para obtener todos los usuarios
    def get_users(self):
        rv = self.mysql_pool.execute("SELECT * from user")  
        data = []
        content = {}
        for result in rv:
            content = {'iduser': result[0], 'username': result[1], 'password': result[2]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para eliminar un usuario
    def delete_user(self, iduser):
        params = {'iduser' : iduser}      
        query = """delete from user where iduser = %(iduser)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
        

################### Actividad ################################
    # Funcion para obtener una actividad por su ID
    def get_actividad(self, id_act):
        params = {'id_act' : id_act}
        rv = self.mysql_pool.execute("SELECT * from actividad where id_act=%(id_act)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_act': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3], 'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todas las actividades
    def get_actividads(self):
        rv = self.mysql_pool.execute("SELECT * from actividad")  
        data = []
        content = {}
        for result in rv:
            content = {'id_act': result[0], 'nombre': result[1], 'descripcion': result[2], 'fecha': result[3], 'hora_inicio': result[4], 'hora_fin': result[5], 'estado': result[6], 'enlace_reu': result[7]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar una actividad
    def add_actividad(self, nombre, descripcion, fecha, hora_inicio, hora_fin, estado, enlace_reu):
        params = {
            'nombre' : nombre,
            'descripcion' : descripcion,
            'fecha' : fecha,
            'hora_inicio' : hora_inicio,
            'hora_fin' : hora_fin,
            'estado' : estado,
            'enlace_reu' : enlace_reu
        }  
        query = """insert into actividad (nombre, descripcion, fecha, hora_inicio, hora_fin, estado, enlace_reu)
            values (%(nombre)s, %(descripcion)s, %(fecha)s, %(hora_inicio)s, %(hora_fin)s, %(estado)s, %(enlace_reu)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_act': cursor.lastrowid, 'nombre': nombre, 'descripcion': descripcion, 'fecha': fecha, 'hora_inicio': hora_inicio, 'hora_fin': hora_fin, 'estado': estado, 'enlace_reu': enlace_reu}
        return data

    # Funcion para eliminar una actividad
    def delete_actividad(self, id_act):
        params = {'id_act' : id_act}      
        query = """delete from actividad where id_act = %(id_act)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


################### Administrador ################################

    # Funcion para obtener un administrador por su ID
    def get_administrador(self, id_adm):
        params = {'id_adm' : id_adm}      
        rv = self.mysql_pool.execute("SELECT * from administrador where id_adm=%(id_adm)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_adm': result[0], 'rol': result[1]}
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
            'rol' : rol
        }  
        query = """insert into administrador (rol)
            values (%(rol)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_adm': cursor.lastrowid, 'rol': rol}
        return data
    
    # Funcion para eliminar un administrador
    def delete_administrador(self, id_adm):
        params = {'id_adm' : id_adm}      
        query = """delete from administrador where id_adm = %(id_adm)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data



################### Contribuidor ################################

    # Funcion para obtener un contribuidor por su ID
    def get_contribuidor(self, id_cont):
        params = {'id_cont' : id_cont}      
        rv = self.mysql_pool.execute("SELECT * from contribuidor where id_cont=%(id_cont)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_cont': result[0], 'nombre': result[1], 'universidad': result[2], 'especialidad': result[3], 'decsripcion': result[4], 'facebool': result[5], 'email': result[6], 'linkedin': result[7], 'rol': result[8]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los contribuidores
    def get_contribuidors(self):
        rv = self.mysql_pool.execute("SELECT * from contribuidor")  
        data = []
        content = {}
        for result in rv:
            content = {'id_cont': result[0], 'nombre': result[1], 'universidad': result[2], 'especialidad': result[3], 'decsripcion': result[4], 'facebool': result[5], 'email': result[6], 'linkedin': result[7], 'rol': result[8]}
            data.append(content)
            content = {}
        return data

    # Funcion para agregar un contribuidor
    def add_contribuidor(self, nombre, universidad, especialidad, decsripcion, facebool, email, linkedin, rol):
        params = {
            'nombre' : nombre,
            'universidad' : universidad,
            'especialidad' : especialidad,
            'decsripcion' : decsripcion,
            'facebool' : facebool,
            'email' : email,
            'linkedin' : linkedin,
            'rol' : rol
        }  
        query = """insert into contribuidor (nombre, universidad, especialidad, decsripcion, facebool, email, linkedin, rol)
            values (%(nombre)s, %(universidad)s, %(especialidad)s, %(decsripcion)s, %(facebool)s, %(email)s, %(linkedin)s, %(rol)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_cont': cursor.lastrowid, 'nombre': nombre, 'universidad': universidad, 'especialidad': especialidad, 'decsripcion': decsripcion, 'facebool': facebool, 'email': email, 'linkedin': linkedin, 'rol': rol}
        return data
    
    # Funcion para eliminar un contribuidor
    def delete_contribuidor(self, id_cont):
        params = {'id_cont' : id_cont}      
        query = """delete from contribuidor where id_cont = %(id_cont)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.create_actividad('prueba 10', 'desde python'))