class User(object):

    db = None

    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM users
            INNER JOIN user_role on user_role.user_id = users.user_id
            INNER JOIN role on user_role.role_id = roles.role_id
        """
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def get(cls, id_data):
        sql = "SELECT * FROM users WHERE users.user_id = %s"
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    @classmethod
    def create(cls, data):
        cursor = cls.db.cursor()
        #Incremento el id en 1 porque la base no es autoincremental
        #cursor.execute("SELECT MAX(id) AS maximum FROM usuario")
        #result = cursor.fetchall()
        #for i in result:
        #    sqlid = i['maximum'] + 1
        sql = """
            INSERT INTO usuario (email, username, password, activo, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (data['email'], data['username'], data['password'], 1, data['first_name'], data['last_name']))
        cls.db.commit()

        return True

    @classmethod
    def update(cls, request):
        sql = """
            UPDATE users
            SET lastname=%s, name=%s, username=%s, email=%s
            WHERE users.user_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql), (request['last_name'], request['first_name'], request['username'], request['email'], request['id_data']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM users WHERE user_id=%s", (id_data,))
        cls.db.commit()
        return True

    @classmethod
    def set_role(cls, usuario_id, rol_id):
        cursor = cls.db.cursor()
        sql = """
            INSERT INTO usuario_tiene_rol (usuario_id, rol_id)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (usuario_id, rol_id))
        cls.db.commit()

        return True

    @classmethod
    def unset_role(cls, usuario_id, rol_id):
        cursor = cls.db.cursor()
        cursor.execute("""
               DELETE FROM usuario_tiene_rol
               WHERE usuario_id = %s and rol_id = %s
            """, (usuario_id, rol_id))
        cursor.execute("DELETE FROM usuario_tiene_rol WHERE usuario_id = %s and rol_id = %s ", (usuario_id, rol_id))
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
        user_id = request['user_id']
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
    def delete_roles(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM usuario_tiene_rol WHERE usuario_id=%s", (id_data,))
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
            SELECT rol.id, rol.nombre FROM usuario_tiene_rol
            INNER JOIN rol ON usuario_tiene_rol.rol_id = rol.id
            WHERE usuario_tiene_rol.usuario_id = %s
        """
        cursor.execute(sql, (id_data))
        data = cursor.fetchall()
        return data

    @classmethod
    def set_rol(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
             rol.nombre FROM usuario_tiene_rol
            INNER JOIN rol ON usuario_tSELECTiene_rol.rol_id = rol.id
            WHERE usuario_tiene_rol.usuario_id = %s
        """
        cursor.execute(sql, (id_data))
        data = cursor.fetchone()
        return data

    @classmethod
    def find_by_username(cls, username):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.username = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username))
        return cursor.fetchone()

    @classmethod
    def find_by_username_not_self(cls, username, id_data):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.username = %s and u.id <> %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username, id_data))
        return cursor.fetchone()


    @classmethod
    def find_by_email(cls, username):
        sql = """
            SELECT * FROM usuario
            WHERE usuario.username = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (username))

        return cursor.fetchone()

    @classmethod
    def find_by_email_not_self(cls, username, id_data):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.username = %s and u.id <> %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (username, id_data))

        return cursor.fetchone()


    @classmethod
    def find_by_id(cls, id_data):
        sql = """
            SELECT * FROM usuario AS u
            WHERE u.id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
    
    @classmethod
    def tiene_rol(cls, id_data, rol):
        data = cls.get_rol(id_data)
        for roles in data:
            if roles['nombre'] == rol:
                return True
        return False
