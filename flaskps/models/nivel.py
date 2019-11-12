class Nivel(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM nivel")
        data = cursor.fetchall()
        return data
    