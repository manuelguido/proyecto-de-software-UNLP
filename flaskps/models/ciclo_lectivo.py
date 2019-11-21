class Ciclo(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM ciclo_lectivo'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
