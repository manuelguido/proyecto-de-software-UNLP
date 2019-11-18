class Rol(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM rol'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()