class User(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM usuario'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def create(cls, data):
        cursor = cls.db.cursor()
        #Incremento el id en 1 porque la base no es autoincremental
        cursor.execute("SELECT MAX(id) AS maximum FROM usuario")
        result = cursor.fetchall()
        for i in result:
            sqlid = i['maximum'] + 1
        sql = """
            INSERT INTO usuario (id, email, password, first_name, last_name, username, activo)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (sqlid, data['email'], data['password'], data['first_name'], data['last_name'], data['username'], data['activo']))
        cls.db.commit()

        return True

    @classmethod
    def find_by_email_and_pass(cls, email, password):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.email = %s AND u.password = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (email, password))

        return cursor.fetchone()

    @classmethod
    def update_user_status(cls, request):
        user_id = request['id']
        activo = request['activo']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE usuario
               SET activo=%s
               WHERE id=%s
            """, (activo, user_id))
        cls.db.commit()

        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM usuario WHERE id=%s", (id_data,))
        cls.db.commit()

        return True

    @classmethod
    def get_permisos(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT permiso.nombre FROM usuario_tiene_rol
            INNER JOIN rol ON usuario_tiene_rol.rol_id = rol.id
            INNER JOIN rol_tiene_permiso ON rol_tiene_permiso.rol_id = rol.id
            INNER JOIN permiso ON rol_tiene_permiso.permiso_id = permiso.id
            WHERE usuario_tiene_rol.usuario_id = %s
        """
        cursor.execute(sql, (id_data))
        data = cursor.fetchall()
        return data

    @classmethod
    def tiene_permiso(cls, id_data, permiso):
        data = cls.get_permisos(id_data)
        for permisos in data:
            if permisos['nombre'] == permiso:
                return True
        return False

    @classmethod
    def get_rol(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT rol.nombre FROM usuario_tiene_rol
            INNER JOIN rol ON usuario_tiene_rol.rol_id = rol.id
            WHERE usuario_tiene_rol.usuario_id = %s
        """
        cursor.execute(sql, (id_data))
        data = cursor.fetchone()
        return data

    @classmethod
    def set_rol(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT rol.nombre FROM usuario_tiene_rol
            INNER JOIN rol ON usuario_tiene_rol.rol_id = rol.id
            WHERE usuario_tiene_rol.usuario_id = %s
        """
        cursor.execute(sql, (id_data))
        data = cursor.fetchone()
        return data