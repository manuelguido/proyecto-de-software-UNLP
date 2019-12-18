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
    def total_paginas_taller(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT *
            FROM estudiante_taller
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
    def allEstudianteTaller(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, estudiante.nombre AS nombreestudiante, estudiante.apellido AS apellidoestudiante, docente.nombre AS nombredocente, docente.apellido AS apellidodocente, taller.nombre AS nombretaller FROM estudiante_taller
            INNER JOIN estudiante ON estudiante.id = estudiante_taller.estudiante_id
            INNER JOIN docente ON docente.id = estudiante_taller.docente_id
            INNER JOIN ciclo_lectivo_taller ON estudiante_taller.ciclo_lectivo_taller_id = ciclo_lectivo_taller.id
            INNER JOIN taller ON estudiante_taller.taller_id = taller.id
            INNER JOIN ciclo_lectivo ON estudiante_taller.ciclo_lectivo_id = ciclo_lectivo.id
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def allEstudianteTallerPaginated(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, estudiante.nombre AS nombreestudiante, estudiante.apellido AS apellidoestudiante, docente.nombre AS nombredocente, docente.apellido AS apellidodocente, taller.nombre AS nombretaller FROM estudiante_taller
            INNER JOIN estudiante ON estudiante.id = estudiante_taller.estudiante_id
            INNER JOIN docente ON docente.id = estudiante_taller.docente_id
            INNER JOIN ciclo_lectivo_taller ON estudiante_taller.ciclo_lectivo_taller_id = ciclo_lectivo_taller.id
            INNER JOIN taller ON estudiante_taller.taller_id = taller.id
            INNER JOIN ciclo_lectivo ON estudiante_taller.ciclo_lectivo_id = ciclo_lectivo.id
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
    def getLastPageTaller(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM estudiante_taller
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
        
    @classmethod
    def estudianteNoEnTaller(cls, data):
        cursor = cls.db.cursor() 
        sql = """
               SELECT *
               FROM estudiante_taller
               WHERE estudiante_taller.estudiante_id=%s and estudiante_taller.docente_responsable_taller_id=%s
            """
        a = cursor.execute(sql, (data['estudiante_id'], data['docente_responsable_taller_id']))
        cls.db.commit()
        if (a>0):
            return False
        else:
            return True

    @classmethod
    def storeEstudianteTaller(cls, data):
        cursor = cls.db.cursor() 
        sql = """
                SELECT *
                FROM docente_responsable_taller
                WHERE docente_responsable_taller.id=%s 
        """
        cursor.execute(sql, (data['docente_responsable_taller_id']))
        taller = cursor.fetchone()
        sql2 = """
                INSERT INTO estudiante_taller (estudiante_id, docente_id, taller_id, ciclo_lectivo_id, ciclo_lectivo_taller_id, docente_responsable_taller_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
        cursor.execute(sql2, (data['estudiante_id'], taller['docente_id'], taller['taller_id'], taller['ciclo_lectivo_id'], taller['ciclo_lectivo_taller_id'], data['docente_responsable_taller_id']))
        cls.db.commit()
        return True

    @classmethod
    def deleteEstudianteTaller(cls, request):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM estudiante_taller WHERE estudiante_id=%s and docente_responsable_taller_id=%s", (request['estudiante_id'],request['docente_responsable_taller_id']))
        cls.db.commit()
        return True


    @classmethod
    def findByClass(cls, id_data):
        sql = """
            SELECT *, clase.id AS clase_id FROM estudiante
            INNER JOIN estudiante_taller ON estudiante_taller.estudiante_id=estudiante.id
            INNER JOIN docente_responsable_taller ON estudiante_taller.docente_responsable_taller_id=docente_responsable_taller.id
            INNER JOIN clase ON clase.docente_responsable_taller_id=docente_responsable_taller.id
            WHERE clase.id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchall()
        