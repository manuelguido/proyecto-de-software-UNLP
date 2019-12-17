class Ciclo(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM ciclo_lectivo ORDER BY año ASC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT *
            FROM ciclo_lectivo
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
            SELECT * FROM ciclo_lectivo ORDER BY año ASC
            LIMIT {limit} offset {offset}
        """
        cursor.execute(sql.format(limit = pagination, offset = (pagination * int(page - 1)) ))
        return cursor.fetchall()

    @classmethod
    def getLastPage(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM ciclo_lectivo
            COUNT
        """
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0

    @classmethod
    def getLastPageCicloLectivo(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM ciclo_lectivo_taller
            COUNT
        """
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0

    @classmethod
    def allCicloTaller(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM ciclo_lectivo_taller
            INNER JOIN taller ON taller.id = ciclo_lectivo_taller.taller_id
            INNER JOIN ciclo_lectivo ON ciclo_lectivo.id = ciclo_lectivo_taller.ciclo_lectivo_id
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO ciclo_lectivo (fecha_ini, fecha_fin, semestre, año)
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data['fecha_ini'], data['fecha_fin'], data['semestre'], data['año']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM ciclo_lectivo WHERE id=%s", (id_data,))
        cls.db.commit()
        cursor.execute("DELETE FROM ciclo_lectivo_taller WHERE ciclo_lectivo_id=%s", (id_data,))
        cls.db.commit()
        cursor.execute("DELETE FROM docente_responsable_taller WHERE ciclo_lectivo_id=%s", (id_data,))
        cls.db.commit()
        cursor.execute("DELETE FROM estudiante_taller WHERE ciclo_lectivo_id=%s", (id_data,))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, request):
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE ciclo_lectivo
               SET fecha_ini=%s, fecha_fin=%s, semestre=%s, año=%s
               WHERE id=%s
            """, (request['fecha_ini'], request['fecha_fin'], request['semestre'], request['año'], request['id_data']))
        cls.db.commit()
        return True

    @classmethod
    def semestreExiste(cls, request):
        cursor = cls.db.cursor()
        a = cursor.execute("""
               SELECT ciclo_lectivo.semestre COUNT
               FROM ciclo_lectivo
               WHERE ciclo_lectivo.semestre=%s and ciclo_lectivo.año=%s
            """, (request['semestre'], request['año']))
        cls.db.commit()
        if (a>0):
            return True
        else:
            return False

    @classmethod
    def cicloNoTieneTaller(cls, data):
        cursor = cls.db.cursor() 
        sql = """
               SELECT taller.id
               FROM taller
               WHERE id=%s
            """
        cursor.execute(sql, (data['taller_id']))
        taller_id = cursor.fetchone()
        sql2 = """
               SELECT ciclo_lectivo.id
               FROM ciclo_lectivo
               WHERE id=%s
            """
        cursor.execute(sql2, (data['ciclo_lectivo_id']))
        ciclo_lectivo_id = cursor.fetchone()
        cursor = cls.db.cursor()
        sql = """
               SELECT ciclo_lectivo_taller.taller_id COUNT
               FROM ciclo_lectivo_taller
               WHERE taller_id=%s and ciclo_lectivo_id=%s
            """
        a = cursor.execute(sql, (taller_id['id'], ciclo_lectivo_id['id']))
        cls.db.commit()
        if (a>0):
            return False
        else:
            return True

    @classmethod
    def getCiclo(cls, id_data):
        sql = """
            SELECT * FROM ciclo_lectivo 
            WHERE ciclo_lectivo.id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()