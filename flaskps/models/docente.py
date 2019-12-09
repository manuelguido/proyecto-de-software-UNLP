class Docente(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, genero.nombre as genero FROM docente
            INNER JOIN genero ON docente.genero_id = genero.id
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT docente.nombre
            FROM docente
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
            SELECT *, genero.nombre as genero FROM docente
            INNER JOIN genero ON docente.genero_id = genero.id
            LIMIT {limit} offset {offset}
        """
        cursor.execute(sql.format(limit = pagination, offset = (pagination * int(page - 1)) ))
        return cursor.fetchall()

    @classmethod
    def searchByFirstName(cls,firstname):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, genero.nombre as genero FROM docente
            INNER JOIN genero ON docente.genero_id = genero.id
            WHERE docente.nombre LIKE '%{firstname}%'
        """
        cursor.execute(sql.format(firstname = firstname))
        return cursor.fetchall()

    @classmethod
    def searchByLastName(cls,lastname):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, genero.nombre as genero FROM docente
            INNER JOIN genero ON docente.genero_id = genero.id
            WHERE docente.apellido LIKE '%{lastname}%'
        """
        cursor.execute(sql.format(lastname = lastname))
        return cursor.fetchall()
    
    @classmethod
    def searchByBoth(cls,firstname,lastname):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, genero.nombre as genero FROM docente
            INNER JOIN genero ON docente.genero_id = genero.id
            WHERE docente.nombre LIKE '%{firstname}%' AND docente.apellido LIKE '%{lastname}%'
        """
        cursor.execute(sql.format(firstname = firstname, lastname = lastname))
        return cursor.fetchall()

    @classmethod
    def getLastPage(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM docente COUNT"
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0


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
