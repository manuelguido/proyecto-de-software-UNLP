class Genero(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM genero")
        data = cursor.fetchall()
        return data
    