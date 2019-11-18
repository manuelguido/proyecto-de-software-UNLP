class Docente(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT  * , genero.nombre as genero FROM docente
            INNER JOIN genero ON docente.genero_id = genero.id
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO docente (apellido, nombre, fecha_nac, localidad_id, domicilio, genero_id, tipo_doc_id, numero, tel)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM docente WHERE id=%s", (id_data,))
        cls.db.commit()

        return True

    @classmethod
    def update(cls, request):
        id_data = request["id"]
        nombre = request["nombre"]
        apellido = request["apellido"]
        fecha_nac = request["fecha_nac"]
        localidad_id = request["localidad_id"]
        domicilio = request["domicilio"]
        genero_id = request["genero_id"]
        tipo_doc_id = request["tipo_doc_id"]
        numero = request["numero"]
        tel = request["tel"]
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE docente
               SET apellido=%s, nombre=%s, fecha_nac=%s, localidad_id=%s, domicilio=%s, genero_id=%s, tipo_doc_id=%s, numero=%s, tel=%s
               WHERE id=%s
            """, (apellido, nombre, fecha_nac, localidad_id, domicilio, genero_id, tipo_doc_id, numero, tel, id_data))
        cls.db.commit()

        return True
