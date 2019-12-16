class Student(object):

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
        """
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT estudiante.nombre
            FROM estudiante
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        count = 0
        for i in result:
            count += 1
            i = i
        paginas = count / paginacion
        if (paginas == 0):
            paginas = 1
        elif not (count % paginacion == 0):
            paginas += 1
        return paginas

    @classmethod
    def allPaginated(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT  *, nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio FROM estudiante
            INNER JOIN nivel ON estudiante.nivel_id = nivel.id
            INNER JOIN genero ON estudiante.genero_id = genero.id
            INNER JOIN escuela ON estudiante.escuela_id = escuela.id
            INNER JOIN barrio ON estudiante.barrio_id = barrio.id
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
            WHERE estudiante.nombre LIKE '%{firstname}%' AND estudiante.apellido LIKE '%{lastname}%'
        """
        cursor.execute(sql.format(firstname = firstname, lastname = lastname))
        return cursor.fetchall()

    @classmethod
    def getLastPage(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT  * FROM estudiante
            COUNT
        """
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO estudiante (apellido, nombre, fecha_nac, localidad_id, nivel_id, domicilio, genero_id, escuela_id, tipo_doc_id, numero, tel, barrio_id, responsable, pmt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE estudiante
               SET apellido=%s, nombre=%s, fecha_nac=%s, localidad_id=%s, nivel_id=%s, domicilio=%s, genero_id=%s, escuela_id=%s, tipo_doc_id=%s, numero=%s, tel=%s, barrio_id=%s, responsable=%s, pmt=%s
               WHERE id=%s
            """, (request['apellido'], request['nombre'], request['fecha_nac'], request['localidad_id'], request['nivel_id'], request['domicilio'], request['genero_id'], request['escuela_id'], request['tipo_doc_id'], request['numero'], request['tel'], request['barrio_id'], request['responsable'], request['pmt'], request['id']))
        cls.db.commit()
        return True
        