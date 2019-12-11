class Nucleo(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM nucleo
        """
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def total_paginas(cls,paginacion):
        cursor = cls.db.cursor()
        sql = """
            SELECT nucleo.nombre FROM nucleo
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
    def getNucleo(cls, id_data):
        sql = """
            SELECT * FROM nucleo 
            WHERE nucleo.id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()