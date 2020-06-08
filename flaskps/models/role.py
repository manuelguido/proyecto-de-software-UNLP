class Role(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM roles")
        return cursor.fetchall()

    @classmethod
    def get_id_by_name(cls, role_name):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM roles WHERE name=%s"
        cursor.execute(sql, (role_name))
        data = cursor.fetchone()
        return data['role_id']
