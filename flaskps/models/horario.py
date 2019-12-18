class Horario(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM horario
        """
        cursor.execute(sql)
        return cursor.fetchall()
