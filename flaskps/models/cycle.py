class Cycle(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM cycles")
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM cycles WHERE cycles.cycle.id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO cycles (fecha_ini, fecha_fin, semestre, año)
            VALUES (%s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data['fecha_ini'], data['fecha_fin'], data['semestre'], data['año']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM cycles WHERE id=%s", (id_data,))
        cls.db.commit()
        cursor.execute("DELETE FROM cycles WHERE cycle_id=%s", (id_data,))
        cls.db.commit()
        cursor.execute("DELETE FROM docente_responsable_taller WHERE cycle_id=%s", (id_data,))
        cls.db.commit()
        cursor.execute("DELETE FROM estudiante_taller WHERE cycles_id=%s", (id_data,))
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
