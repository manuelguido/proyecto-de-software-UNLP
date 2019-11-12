class TipoDoc(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM tipo_doc")
        data = cursor.fetchall()
        return data
    