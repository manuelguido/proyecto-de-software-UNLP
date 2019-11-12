class Localidad(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM localidad")
        data = cursor.fetchall()
        return data
    