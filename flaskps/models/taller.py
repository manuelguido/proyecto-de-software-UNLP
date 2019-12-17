class Taller(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM taller'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()

    @classmethod
    def tallerNoTieneDocente(cls, data):
        cursor = cls.db.cursor() 
        sql = """
               SELECT *
               FROM taller
               WHERE id=%s
            """
        cursor.execute(sql, (data['taller_id']))
        taller = cursor.fetchone()
        sql2 = """
               SELECT docente.id
               FROM docente
               WHERE id=%s
            """
        cursor.execute(sql2, (data['docente_id']))
        docente_id = cursor.fetchone()
        cursor = cls.db.cursor()
        sql = """
               SELECT docente_responsable_taller.taller_id COUNT
               FROM docente_responsable_taller
               WHERE taller_id=%s and docente_id=%s
            """
        a = cursor.execute(sql, (taller['id'], docente_id['id']))
        cls.db.commit()
        if (a>0):
            return False
        else:
            return True

    @classmethod
    def deleteTallerCiclo(cls, request):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM ciclo_lectivo_taller WHERE ciclo_lectivo_id=%s", (request['ciclo_lectivo_id'],))
        cls.db.commit()
        cursor.execute("DELETE FROM docente_responsable_taller WHERE ciclo_lectivo_id=%s", (request['taller_id'],))
        cls.db.commit()
        cursor.execute("DELETE FROM estudiante_taller WHERE ciclo_lectivo_id=%s", (request['ciclo_lectivo_id'],))
        cls.db.commit()
        return True


    @classmethod
    def storeConDocente(cls, data):
        cursor = cls.db.cursor() 
        sql = """
               SELECT taller.id
               FROM taller
               WHERE id=%s
            """
        cursor.execute(sql, (data['taller_id']))
        taller_id = cursor.fetchone()
        sql2 = """
               SELECT docente.id
               FROM docente
               WHERE id=%s
            """
        cursor.execute(sql2, (data['docente_id']))
        docente_id = cursor.fetchone()

        sql3 = """
               SELECT ciclo_lectivo.id
               FROM taller
               WHERE id=%s
            """
        cursor.execute(sql, (data['taller_id']))
        taller_id = cursor.fetchone()



        sql3 = """
            INSERT INTO docente_responsable_taller (taller_id, docente_id)
            VALUES (%s, %s)
        """
        cursor.execute(sql3, (taller_id['id'], docente_id['id']))
        cls.db.commit()
        return True
