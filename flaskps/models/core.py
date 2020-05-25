class Core(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM cores")
        data = cursor.fetchall()
        return data

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM cores WHERE cores.core_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
