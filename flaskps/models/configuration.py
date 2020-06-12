class Configuration(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT * FROM configuration")
        return cursor.fetchall()

    @classmethod
    def update(cls, data):
        cursor = cls.db.cursor()
        sql = "UPDATE configuration SET active=%s, title=%s, description=%s, email=%s"
        cursor.execute(sql, (data['active'], data['title'], data['description'], data['email']))
        cls.db.commit()
        return True
