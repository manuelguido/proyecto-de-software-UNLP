class Nucleo(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT  * , nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio  FROM estudiante
            INNER JOIN nivel ON estudiante.nivel_id = nivel.id
            INNER JOIN genero ON estudiante.genero_id = genero.id
            INNER JOIN escuela ON estudiante.escuela_id = escuela.id
            INNER JOIN barrio ON estudiante.barrio_id = barrio.id
            LEFT JOIN responsable ON responsable.id = estudiante.responsable_id
        """
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT nucleo.nombre
            FROM nucleo
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        count = 0
        for i in result:
            count += 1
            i = i
        paginas = count / paginacion 
        if not (count % paginacion == 0):
            paginas += 1
        return paginas

    @classmethod
    def allPaginated(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM nucleo
            LIMIT {limit} offset {offset}
        """
        cursor.execute(sql.format(limit = pagination, offset = (pagination * int(page - 1)) ))
        return cursor.fetchall()

    @classmethod
    def searchByFirstName(cls,firstname):
        cursor = cls.db.cursor()
        sql = """
            SELECT  * , nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio  FROM estudiante
            INNER JOIN nivel ON estudiante.nivel_id = nivel.id
            INNER JOIN genero ON estudiante.genero_id = genero.id
            INNER JOIN escuela ON estudiante.escuela_id = escuela.id
            INNER JOIN barrio ON estudiante.barrio_id = barrio.id
            LEFT JOIN responsable ON responsable.id = estudiante.responsable_id
            WHERE estudiante.nombre LIKE '%{firstname}%'
        """
        cursor.execute(sql.format(firstname = firstname))
        return cursor.fetchall()

    @classmethod
    def searchByLastName(cls,lastname):
        cursor = cls.db.cursor()
        sql = """
            SELECT  * , nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio  FROM estudiante
            INNER JOIN nivel ON estudiante.nivel_id = nivel.id
            INNER JOIN genero ON estudiante.genero_id = genero.id
            INNER JOIN escuela ON estudiante.escuela_id = escuela.id
            INNER JOIN barrio ON estudiante.barrio_id = barrio.id
            LEFT JOIN responsable ON responsable.id = estudiante.responsable_id
            WHERE estudiante.apellido LIKE '%{lastname}%'
        """
        cursor.execute(sql.format(lastname = lastname))
        return cursor.fetchall()
    
    @classmethod
    def searchByBoth(cls,firstname,lastname):
        cursor = cls.db.cursor()
        sql = """
            SELECT  * , nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio  FROM estudiante
            INNER JOIN nivel ON estudiante.nivel_id = nivel.id
            INNER JOIN genero ON estudiante.genero_id = genero.id
            INNER JOIN escuela ON estudiante.escuela_id = escuela.id
            INNER JOIN barrio ON estudiante.barrio_id = barrio.id
            LEFT JOIN responsable ON responsable.id = estudiante.responsable_id
            WHERE estudiante.nombre LIKE '%{firstname}%' AND estudiante.apellido LIKE '%{lastname}%'
        """
        cursor.execute(sql.format(firstname = firstname, lastname = lastname))
        return cursor.fetchall()

    @classmethod
    def getLastPage(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM nucleo
            COUNT
        """
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO estudiante (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, responsable_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
        responsable_id = request['responsable_id']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE estudiante
               SET apellido=%s, nombre=%s, fecha_nac=%s, localidad_id=%s, nivel_id=%s, domicilio=%s, genero_id=%s, escuela_id=%s, tipo_doc_id=%s, numero=%s, tel=%s, barrio_id=%s, responsable_id=%s
               WHERE id=%s
            """, (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, responsable_id, id_data))
        cls.db.commit()
        return True
        