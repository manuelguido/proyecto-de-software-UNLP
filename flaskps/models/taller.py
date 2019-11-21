class Taller(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM taller'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
