class User(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM usuario'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT usuario.first_name
            FROM usuario
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        count = 0
        for i in result:
            count += 1
            i = i
        paginas = count / paginacion 
        if not (count % paginacion == 0):
            paginas += 1
        return paginas

    @classmethod
    def allPaginated(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM usuario
            LIMIT {limit} offset {offset}
        """
        cursor.execute(sql.format(limit = pagination, offset = (pagination * int(page - 1)) ))
        return cursor.fetchall()

    @classmethod
    def searchByUserName(cls,firstname):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM usuario
            WHERE usuario.username LIKE '%{firstname}%'
        """
        cursor.execute(sql.format(firstname = firstname))
        return cursor.fetchall()

    #@classmethod
    #def searchByActive(cls,ac):
    #    cursor = cls.db.cursor()
    #    sql = """
    #        SELECT * FROM usuario
    #        WHERE usuario.activo = %s
    #    """
    #    print(ac)
    #    #cursor.execute(sql, (ac))
    #    #return cursor.fetchall()

    @classmethod
    def getLastPage(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM usuario
            COUNT
        """
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0

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