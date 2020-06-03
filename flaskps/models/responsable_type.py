class ResponsableType(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM responsable_types")
        return cursor.fetchall()
    