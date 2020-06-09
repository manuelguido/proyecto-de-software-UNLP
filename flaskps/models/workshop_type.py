class WorkshopType(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = 'SELECT * FROM workshop_types'
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM workshop_types WHERE workshop_type_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
