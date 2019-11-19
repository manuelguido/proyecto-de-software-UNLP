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
        sql = """
            INSERT INTO usuario (email, password, first_name, last_name)
            VALUES (%s, %s, %s, %s)
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
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
    def get_roles(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM usario_tiene_rol
            INNER JOIN rol ON usuario_tiene_rol.rol_id = rol.id
            WHERE usuario_tiene_rol.usuario_id = %s
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
