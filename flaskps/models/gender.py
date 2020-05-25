class Gender(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM genders")
        data = cursor.fetchall()
        return data

    @classmethod
    def get_day(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM genders WHERE genders.gender_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
