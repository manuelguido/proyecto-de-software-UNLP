class Ciclo(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM ciclo_lectivo
        """
        cursor.execute(sql)
        return cursor.fetchall()
    
    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO ciclo_lectivo (fecha_ini, fecha_fin, semestre)
            VALUES (%s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM ciclo_lectivo WHERE id=%s", (id_data,))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, request):
        fecha_ini = request['fecha_ini']
        fecha_fin = request['fecha_fin']
        semestre = request['semestre']
        id_data = request['id_data']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE ciclo_lectivo
               SET fecha_ini=%s, fecha_fin=%s, semestre=%s
               WHERE id=%s
            """, (fecha_ini, fecha_fin, semestre, id_data))
        cls.db.commit()
        return True
        
    @classmethod
    def semestreNoExiste(cls, request):
        cursor = cls.db.cursor()
        a = cursor.execute("""
               SELECT ciclo_lectivo.semestre COUNT
               FROM ciclo_lectivo
               WHERE ciclo_lectivo.semestre=%s
            """, (request['semestre']))
        cls.db.commit()
        if (a>0):
            return False
        else:
            return True
    