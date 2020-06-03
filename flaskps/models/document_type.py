class DocumentType(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM document_types")
        return cursor.fetchall()
    