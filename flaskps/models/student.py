class Student(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT  * , localidad.nombre as localidad, nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, tipo_doc.nombre as tipo_doc, barrio.nombre as barrio  FROM estudiante
            INNER JOIN localidad ON estudiante.localidad_id = localidad.id
            INNER JOIN nivel ON estudiante.nivel_id = nivel.id
            INNER JOIN genero ON estudiante.genero_id = genero.id
            INNER JOIN escuela ON estudiante.escuela_id = escuela.id
            INNER JOIN tipo_doc ON estudiante.tipo_doc_id = tipo_doc.id
            INNER JOIN barrio ON estudiante.barrio_id = barrio.id
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO estudiante (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM estudiante WHERE id=%s", (id_data,))
        cls.db.commit()

        return True

    @classmethod
    def update(cls, request):
        id_data = request['id']
        apellido = request['apellido']
        nombre = request['nombre']
        fecha_nac = request['fecha_nac']
        localidad_id = request['localidad_id']
        nivel_id = request['nivel_id']
        domicilio = request['domicilio']
        genero_id = request['genero_id']
        escuela_id = request['escuela_id']
        tipo_doc_id = request['tipo_doc_id']
        numero = request['numero']
        tel = request['tel']
        barrio_id = request['barrio_id']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE estudiante
               SET apellido=%s, nombre=%s, fecha_nac=%s, localidad_id=%s, nivel_id=%s, domicilio=%s, genero_id=%s, escuela_id=%s, tipo_doc_id=%s, numero=%s, tel=%s, barrio_id=%s
               WHERE id=%s
            """, (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, id_data))
        cls.db.commit()

        return True
