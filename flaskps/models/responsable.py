class Responsable(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT *
            FROM responsable
        """
        cursor.execute(sql)
        return cursor.fetchall()