class User(object):

    db = None

    #Retorna todos los usuarios
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
    
    #Retorna el usuario
    @classmethod
    def get(cls, id_data):
        sql = "SELECT * FROM users WHERE users.user_id = %s"
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    #Crea un usuario
    @classmethod
    def create(cls, data):
        cursor = cls.db.cursor()
        sql = """
             INSERT INTO users (name, lastname, username, email, password, active)
             VALUES (%s, %s, %s, %s, %s, %s)
         """
        cursor.execute(sql, (data['name'], data['lastname'], data['username'], data['email'], data['password'], 1))
        cls.db.commit()
        return True

    #Actualiza un usuario
    @classmethod
    def update(cls, request):
        sql = """
            UPDATE users
            SET name=%s, lastname=%s, username=%s, email=%s
            WHERE users.user_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (request['name'], request['lastname'], request['username'], request['email'], request['user_id']))
        cls.db.commit()
        return True

    #Elimina un usuario
    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM users WHERE user_id=%s", (id_data,))
        cls.db.commit()
        return True

    #Retorna los pemisos del usuario
    @classmethod
    def permissions(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT permissions.name FROM permissions
            INNER JOIN role_permission ON role_permission.permission_id = permissions.permission_id
            INNER JOIN roles ON roles.role_id = role_permission.role_id
            INNER JOIN user_role ON user_role.role_id = roles.role_id
            WHERE user_role.user_id = %s
        """
        cursor.execute(sql, (id_data))
        return cursor.fetchall()

    @classmethod
    def has_permission(cls, id_data, perm):
        permissions = cls.permissions(id_data)
        for permission in permissions:
            if permission['name'] == perm:
                return True
        return False

    @classmethod
    def get_by_email(cls, email):
        sql = """
            SELECT * FROM users
            WHERE users.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email))

        return cursor.fetchone()

    #Crea un usuario
    @classmethod
    def create_by_google(cls, data):
        cursor = cls.db.cursor()
        sql = """
             INSERT INTO users (name, lastname, username, email, active, google_user)
             VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (data['given_name'], data['family_name'], data['email'], data['email'], 1, 1))
        cls.db.commit()
        return True

    #Retorna True si el usuario tiene al menos un rol, sino retorna False
    @classmethod
    def has_roles(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM user_role
            INNER JOIN roles ON user_role.role_id = roles.role_id
            WHERE user_role.user_id = %s
        """
        cursor.execute(sql, (id_data))
        roles = cursor.fetchall()
        count = 0
        for i in roles:
            count += 1
        if (count > 0):
            return True
        else:
            return False

    #Retorna los roles del usuario
    @classmethod
    def get_roles(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM user_role
            INNER JOIN role ON user_role.role_id = roles.role_id
            WHERE user_role.user_id = %s
        """
        cursor.execute(sql, (id_data))
        data = cursor.fetchall()
        return data














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
            SELECT * FROM users
            WHERE users.email = %s AND users.password = %s
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
