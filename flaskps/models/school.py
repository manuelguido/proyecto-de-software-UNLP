class School(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM escuela")
        data = cursor.fetchall()
        return data
    