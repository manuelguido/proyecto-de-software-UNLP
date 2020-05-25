class Role(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM roles'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
