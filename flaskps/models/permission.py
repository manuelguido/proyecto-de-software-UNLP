class Permission(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM permissions'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()
