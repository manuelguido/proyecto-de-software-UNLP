class CycleWorkshop(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = 'SELECT * FROM cycle_workshop'
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM cycle_workshop WHERE cycle_workshop_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
