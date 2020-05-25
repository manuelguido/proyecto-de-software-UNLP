class Instrument(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM instrument
            INNER JOIN instrument_types ON instrument_types.instrument_type_id = instrument_types.instrument_type_id
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM instruments WHERE instruments.instrument_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO instrumento (nombre, tipo_id, codigo)
            VALUES (%s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data['nombre'], data['tipo_instrumento'], data['codigo']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM instrumento WHERE id=%s", (id_data,))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, request):
        id_data = request['id_data']
        nombre = request['nombre']
        codigo = request['codigo']
        tipo_id = request['tipo_instrumento']
        #img = request['img']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE instrumento
               SET nombre=%s, codigo=%s, tipo_id=%s
               WHERE id=%s
            """, (nombre, codigo, tipo_id, id_data))
        cls.db.commit()
        return True
        
