class Clase(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, taller.nombre AS nombretaller, nucleo.nombre AS nombrenucleo, docente.nombre AS nombredocente, docente.apellido AS apellidodocente FROM clase
            INNER JOIN horario ON horario.id=clase.horario_id
            INNER JOIN docente_responsable_taller ON docente_responsable_taller.id=clase.docente_responsable_taller_id
            INNER JOIN docente ON docente_responsable_taller.docente_id=docente.id
            INNER JOIN ciclo_lectivo ON ciclo_lectivo.id=docente_responsable_taller.ciclo_lectivo_id
            INNER JOIN taller ON docente_responsable_taller.taller_id = taller.id
            INNER JOIN nucleo ON nucleo.id=clase.nucleo_id
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO clase (nucleo_id, dia, docente_responsable_taller_id, horario_id)
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data['nucleo_id'], data['dia'], data['docente_responsable_taller_id'], data['horario_id']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM clase WHERE id=%s", (id_data,))
        cls.db.commit()
        return True

    @classmethod
    def noExiste(cls, data):
        cursor = cls.db.cursor() 
        sql = """
               SELECT *
               FROM clase
               WHERE nucleo_id=%s and dia=%s and docente_responsable_taller_id=%s and horario_id=%s
            """
        a = cursor.execute(sql, (data['nucleo_id'], data['dia'], data['docente_responsable_taller_id'], data['horario_id'],))
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
    def findClass(cls, id_data):
        sql = """
            SELECT *, taller.nombre AS nombretaller, nucleo.nombre AS nombrenucleo, docente.nombre AS nombredocente, docente.apellido AS apellidodocente FROM clase
            INNER JOIN horario ON horario.id=clase.horario_id
            INNER JOIN docente_responsable_taller ON docente_responsable_taller.id=clase.docente_responsable_taller_id
            INNER JOIN docente ON docente_responsable_taller.docente_id=docente.id
            INNER JOIN ciclo_lectivo ON ciclo_lectivo.id=docente_responsable_taller.ciclo_lectivo_id
            INNER JOIN taller ON docente_responsable_taller.taller_id = taller.id
            INNER JOIN nucleo ON nucleo.id=clase.nucleo_id
            WHERE clase.id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()