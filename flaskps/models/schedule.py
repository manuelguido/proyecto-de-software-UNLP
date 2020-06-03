class Schedule(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM schedules")
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM schedules WHERE schedules.schedule_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
