class Student(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM estudiante")
        data = cursor.fetchall()
        return data

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO estudiante (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
        id_data = request.form['id']
        apellido = request.form['apellido']
        nombre = request.form['nombre']
        fecha_nac = request.form['fecha_nac']
        localidad_id = request.form['localidad_id']
        nivel_id = request.form['nivel_id']
        domicilio = request.form['domicilio']
        genero_id = request.form['genero_id']
        escuela_id = request.form['escuela_id']
        tipo_doc_id = request.form['tipo_doc_id']
        numero = request.form['numero']
        tel = request.form['tel']
        barrio_id = request.form['barrio_id']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE estudiante
               SET apellido=%s, nombre=%s, fecha_nac=%s, localidad_id=%s, nivel_id=%s, domicilio=%s, genero_id=%s, escuela_id=%s, tipo_doc_id=%s, numero=%s, tel=%s, barrio_id=%s
               WHERE id=%s
            """, (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, id_data))
        cls.db.commit()

        return True
