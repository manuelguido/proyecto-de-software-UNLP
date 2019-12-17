class Taller(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM taller'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def allCicloTallerPaginated(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM ciclo_lectivo_taller
            INNER JOIN taller ON taller.id = ciclo_lectivo_taller.taller_id
            INNER JOIN ciclo_lectivo ON ciclo_lectivo.id = ciclo_lectivo_taller.ciclo_lectivo_id
            LIMIT {limit} offset {offset}
        """
        cursor.execute(sql.format(limit = pagination, offset = (pagination * int(page - 1)) ))
        return cursor.fetchall()

    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT *
            FROM ciclo_lectivo_taller
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
    def storeConTaller(cls, data):
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
        sql3 = """
            INSERT INTO ciclo_lectivo_taller (taller_id, ciclo_lectivo_id)
            VALUES (%s, %s)
        """
        cursor.execute(sql3, (taller_id['id'], ciclo_lectivo_id['id']))
        cls.db.commit()
        return True

    @classmethod
    def deleteTallerCiclo(cls, request):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM ciclo_lectivo_taller WHERE ciclo_lectivo_id=%s and taller_id=%s", (request['ciclo_lectivo_id'],request['taller_id']))
        cls.db.commit()
        cursor.execute("DELETE FROM docente_responsable_taller WHERE ciclo_lectivo_id=%s and taller_id=%s", (request['ciclo_lectivo_id'],request['taller_id']))
        cls.db.commit()
        cursor.execute("DELETE FROM estudiante_taller WHERE ciclo_lectivo_id=%s and taller_id=%s", (request['ciclo_lectivo_id'],request['taller_id']))
        cls.db.commit()
        return True

    @classmethod
    def getLastPage(cls,pagination,page):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM ciclo_lectivo_taller COUNT"
        if ((cursor.execute(sql) / pagination) <= page):
            return 1
        else:
            return 0
