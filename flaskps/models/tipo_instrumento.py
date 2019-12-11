class TipoInstrumento(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM tipo_instrumento
        """
        cursor.execute(sql)
        return cursor.fetchall()