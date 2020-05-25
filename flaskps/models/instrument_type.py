class InstrumentType(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM instrument_types")
        data = cursor.fetchall()
        return data

    @classmethod
    def get_day(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM instrument_types WHERE instrument_types.instrument_type_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
