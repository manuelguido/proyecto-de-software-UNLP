class Responsable(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM responsables")
        return cursor.fetchall()

    @classmethod
    def create(cls, data):
        sql = """
            INSERT INTO responsables (lastname, name, phone, responsable_type_id)
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data['responsable_lastname'], data['responsable_name'], data['responsable_phone'], data['responsable_type_id']))
        cls.db.commit()
        return cursor.lastrowid
