class User(object):

    db = None

    #---------------------------------------------------#
    #   Retorna todos los usuarios
    #---------------------------------------------------#
    @classmethod
    def all(cls):
        sql = """
            SELECT users.user_id, users.name, users.lastname, users.username, users.email, users.active
            FROM users
        """
        cursor = cls.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
    #---------------------------------------------------#
    #   Retorna un usuario por user_id
    #---------------------------------------------------#
    @classmethod
    def get(cls, user_id):
        sql = """
            SELECT * FROM users WHERE users.user_id = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (user_id))
        return cursor.fetchone()

    #---------------------------------------------------#
    #   Crea un usuario
    #---------------------------------------------------#
    @classmethod
    def create(cls, user, password):
        cursor = cls.db.cursor()
        sql = """
             INSERT INTO users (name, lastname, username, email, password, active)
             VALUES (%s, %s, %s, %s, %s, %s)
         """
        cursor.execute(sql, (user['name'], user['lastname'], user['username'], user['email'], password, user['active']))
        cls.db.commit()
        return True

    #---------------------------------------------------#
    #   Actualiza un usuario
    #---------------------------------------------------#
    @classmethod
    def update(cls, user):
        sql = """
            UPDATE users
            SET name=%s, lastname=%s, username=%s, email=%s, active=%s 
            WHERE users.user_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (user['name'], user['lastname'], user['username'], user['email'], user['active'], user['user_id']))
        cls.db.commit()
        return True

    #---------------------------------------------------#
    #   Elimina un usuario
    #---------------------------------------------------#
    @classmethod
    def delete(cls, user_id):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM users WHERE user_id=%s", (user_id))
        cls.db.commit()
        return True

    #---------------------------------------------------#
    #   Retorna todos los permisos del usuario
    #---------------------------------------------------#
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

    #---------------------------------------------------#
    #   Chequea que un usuario tenga un determinado permiso
    #---------------------------------------------------#
    @classmethod
    def has_permission(cls, id_data, perm):
        permissions = cls.permissions(id_data)
        for permission in permissions:
            if permission['name'] == perm:
                return True
        return False

    #---------------------------------------------------#
    #   Crea un usuario loggeado mediante oAuth by Google
    #---------------------------------------------------#
    @classmethod
    def create_by_google(cls, data):
        cursor = cls.db.cursor()
        sql = """
             INSERT INTO users (name, lastname, username, email, active, google_user)
             VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (data['given_name'], data['family_name'], data['email'], data['email'], 1, 1))
        cls.db.commit()
        return True

    #---------------------------------------------------#
    #   Retorna true si el usuario tiene al menos un rol
    #---------------------------------------------------#
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

    #---------------------------------------------------#
    #   Retorna todos los roles del usuario
    #---------------------------------------------------#
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

    #---------------------------------------------------#
    #   Chequea que un usuario tenga un determinado rol
    #---------------------------------------------------#
    @classmethod
    def has_role(cls, user_id, role_id):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM user_role
            WHERE user_role.user_id = %s AND user_role.role_id = %s
        """
        cursor.execute(sql, (user_id, role_id))
        return cursor.fetchone()

    #---------------------------------------------------#
    #   Agrega un rol a un usuario
    #---------------------------------------------------#
    @classmethod
    def add_role(cls, user_id, role_id):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM user_role
            WHERE user_id=%s AND role_id=%s
        """
        cursor.execute(sql, (user_id, role_id))
        result = cursor.fetchone()

        if (not result):
            sql = """
                INSERT INTO user_role (user_id, role_id)
                VALUES (%s, %s)
            """
            cursor.execute(sql, (user_id, role_id))
            cls.db.commit()
            return True

    #---------------------------------------------------#
    #   Elimina un rol de un usuario
    #---------------------------------------------------#
    @classmethod
    def remove_role(cls, user_id, role_id):
        cursor = cls.db.cursor()
        sql = """
               DELETE FROM user_role
               WHERE user_id = %s and role_id = %s
            """
        cursor.execute(sql, (user_id, role_id))
        cls.db.commit()
        return True

    #---------------------------------------------------#
    #   Actualiza el estado de un usuario
    #---------------------------------------------------#
    @classmethod
    def update_user_status(cls, user):
        cursor = cls.db.cursor()
        sql = "UPDATE users SET active=%s WHERE user_id=%s"
        cursor.execute(sql, (user['active'], user['user_id']))
        cls.db.commit()
        return True

    #---------------------------------------------------#
    #   Elimina todos los roles de un usuario
    #---------------------------------------------------#
    @classmethod
    def remove_roles(cls, user_id):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM user_role WHERE user_id=%s", (user_id))
        cls.db.commit()
        return True

    #---------------------------------------------------#
    #   Obtiene un usuario por email y contraseña
    #---------------------------------------------------#
    @classmethod
    def find_by_email_and_pass(cls, email, password):
        sql = """
            SELECT * FROM users
            WHERE users.email = %s AND users.password = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (email, password))

        return cursor.fetchone()

    #---------------------------------------------------#
    #   Encontrar usuario por username
    #---------------------------------------------------#
    @classmethod
    def find_by_username(cls, username):
        sql = """
            SELECT * FROM users
            WHERE users.username = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username))
        return cursor.fetchone()

    #---------------------------------------------------#
    #   Obtiene un usuario por email o username
    #---------------------------------------------------#
    @classmethod
    def find_by_email_or_username(cls, data):
        sql = "SELECT * FROM users WHERE users.email = %s OR users.username = %s"
        cursor = cls.db.cursor()
        cursor.execute(sql, (data, data))
        return cursor.fetchone()

    #---------------------------------------------------#
    #   Chequear que el username no esté en uso
    #---------------------------------------------------#
    @classmethod
    def find_by_username_not_self(cls, user):
        sql = """
            SELECT * FROM users
            WHERE username = %s and user_id <> %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (user['username'], user['user_id']))
        return cursor.fetchone()

    #---------------------------------------------------#
    #   Encontrar usuario por email
    #---------------------------------------------------#
    @classmethod
    def find_by_email(cls, username):
        sql = """
            SELECT * FROM users
            WHERE users.email = %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (username))
        return cursor.fetchone()

    #---------------------------------------------------#
    #   Chequear que el email no esté en uso
    #---------------------------------------------------#
    @classmethod
    def find_by_email_not_self(cls, user):
        sql = """
            SELECT * FROM users
            WHERE email = %s and user_id <> %s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (user['username'], user['user_id']))
        return cursor.fetchone()
