class Barrio(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM barrio")
        data = cursor.fetchall()
        return data
    