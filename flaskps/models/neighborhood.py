class Neighborhood(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM neighborhoods")
        return cursor.fetchall()

    