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
    def allCicloTaller(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM ciclo_lectivo_taller
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
