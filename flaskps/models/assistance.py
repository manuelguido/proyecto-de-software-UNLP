class Assistance(object):

    db = None

    @classmethod
    def all(cls, lesson_id):
        cursor = cls.db.cursor()
        sql = """
            SELECT DISTINCT
            students.name, students.lastname, students.document_number,
            document_types.name AS document_type,
            assistances.date, assistances.present,
            schedules.hour_from, schedules.hour_to,
            days.name AS day,
            teachers.name AS teacher_name, teachers.lastname AS teacher_lastname,
            cores.name AS core
            FROM assistances
            INNER JOIN schedules ON schedules.schedule_id = assistances.schedule_id
            INNER JOIN students ON students.student_id = assistances.student_id
            INNER JOIN document_types ON students.document_type_id = document_types.document_type_id
            INNER JOIN teachers ON assistances.teacher_id = teachers.teacher_id
            INNER JOIN cores ON schedules.core_id = cores.core_id
            INNER JOIN days ON schedules.day_id = days.day_id
            WHERE schedules.lesson_id = %s
            ORDER BY assistances.date
        """
        cursor.execute(sql, (lesson_id))
        return cursor.fetchall()

    @classmethod
    def wrong_student(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT lesson_student.lesson_id COUNT
            FROM lesson_student
            WHERE lesson_id=%s and student_id=%s
        """
        result = cursor.execute(sql, (data['lesson_id'], data['student_id']))
        cls.db.commit()
        return (result == 0)

    @classmethod
    def add(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT assistances.student_id COUNT
            FROM assistances
            WHERE assistances.teacher_id=%s and assistances.student_id=%s and assistances.schedule_id=%s and assistances.date=%s
        """
        result = cursor.execute(sql, (data['teacher_id'], data['student_id'], data['schedule_id'], data['date']))
        cls.db.commit()
        if (result == 0):
            sql = """
                INSERT
                INTO assistances (teacher_id, student_id, schedule_id, date, present)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (data['teacher_id'], data['student_id'], data['schedule_id'], data['date'], data['present']))
            cls.db.commit()

        return True

    # @classmethod
    # def all(cls):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT *, taller.nombre AS nombretaller, nucleo.nombre AS nombrenucleo FROM asistencia
    #         INNER JOIN horario ON horario.id=clase.horario_id
    #         INNER JOIN docente_responsable_taller ON docente_responsable_taller.id=clase.docente_responsable_taller_id
    #         INNER JOIN taller ON docente_responsable_taller.taller_id = taller.id
    #         INNER JOIN nucleo ON nucleo.id=clase.nucleo_id
    #     """
    #     cursor.execute(sql)
    #     return cursor.fetchall()

    # @classmethod
    # def store(cls, data):
    #     sql = """
    #         INSERT INTO clase (nucleo_id, dia, docente_responsable_taller_id, horario_id)
    #         VALUES (%s, %s, %s, %s)
    #     """
    #     cursor = cls.db.cursor()
    #     cursor.execute(sql, (data['nucleo_id'], data['dia'], data['docente_responsable_taller_id'], data['horario_id']))
    #     cls.db.commit()
    #     return True

    # @classmethod
    # def delete(cls, id_data):
    #     cursor = cls.db.cursor()
    #     cursor.execute("DELETE FROM clase WHERE id=%s", (id_data,))
    #     cls.db.commit()
    #     return True

    # @classmethod
    # def noExiste(cls, data):
    #     cursor = cls.db.cursor() 
    #     sql = """
    #            SELECT *
    #            FROM asistencia_estudiante_taller
    #            WHERE clase_id=%s and fecha=%s and estudiante_id=%s
    #         """
    #     a = cursor.execute(sql, (data['clase_id'], data['fecha'], data['estudiante_id'],))
    #     cls.db.commit()
    #     if (a>0):
    #         return False
    #     else:
    #         return True

    # @classmethod
    # def storeEstudianteTaller(cls, data):
    #     cursor = cls.db.cursor() 
    #     sql = """
    #             SELECT *
    #             FROM docente_responsable_taller
    #             WHERE docente_responsable_taller.id=%s 
    #     """
    #     cursor.execute(sql, (data['docente_responsable_taller_id']))
    #     taller = cursor.fetchone()
    #     sql2 = """
    #             INSERT INTO estudiante_taller (estudiante_id, docente_id, taller_id, ciclo_lectivo_id, ciclo_lectivo_taller_id, docente_responsable_taller_id)
    #             VALUES (%s, %s, %s, %s, %s, %s)
    #         """
    #     cursor.execute(sql2, (data['estudiante_id'], taller['docente_id'], taller['taller_id'], taller['ciclo_lectivo_id'], taller['ciclo_lectivo_taller_id'], data['docente_responsable_taller_id']))
    #     cls.db.commit()
    #     return True

    # @classmethod
    # def deleteEstudianteTaller(cls, request):
    #     cursor = cls.db.cursor()
    #     cursor.execute("DELETE FROM estudiante_taller WHERE estudiante_id=%s and docente_responsable_taller_id=%s", (request['estudiante_id'],request['docente_responsable_taller_id']))
    #     cls.db.commit()
    #     return True

    # @classmethod
    # def getAsistencias(cls, data):
    #     sql = """
    #         SELECT * FROM asistencia_estudiante_taller
    #         INNER JOIN estudiante ON estudiante.id=asistencia_estudiante_taller.estudiante_id
    #         INNER JOIN clase ON clase.id=asistencia_estudiante_taller.clase_id
    #         INNER JOIN horario ON horario.id=clase.horario_id
    #         WHERE clase.id=%s and clase.horario_id=%s
    #     """
    #     cursor = cls.db.cursor()
    #     cursor.execute(sql, (data['id'], data['horario_id']))
    #     return cursor.fetchall()

    # @classmethod
    # def storeAsistencia(cls, data):
    #     cursor = cls.db.cursor() 
    #     sql = """
    #         SELECT * FROM clase
    #         INNER JOIN docente_responsable_taller ON docente_responsable_taller.id=clase.docente_responsable_taller_id
    #         INNER JOIN estudiante_taller ON estudiante_taller.docente_responsable_taller_id=docente_responsable_taller.id and docente_responsable_taller.ciclo_lectivo_taller_id=estudiante_taller.ciclo_lectivo_taller_id
    #         WHERE clase.id=%s
    #     """
    #     cursor.execute(sql, (data['clase_id']))
    #     clase = cursor.fetchone()
    #     sql2 = """
    #         INSERT INTO asistencia_estudiante_taller (estudiante_id, clase_id, fecha, docente_responsable_taller_id, ciclo_lectivo_id, presente)
    #         VALUES (%s, %s, %s, %s, %s, %s)
    #     """
    #     cursor.execute(sql2, (data['estudiante_id'], data['clase_id'], data['fecha'], clase['docente_responsable_taller_id'], clase['ciclo_lectivo_id'], '1'))
    #     cls.db.commit()
    #     return True

    # @classmethod
    # def storeInasistencia(cls, data):
    #     cursor = cls.db.cursor() 
    #     sql = """
    #         SELECT * FROM clase
    #         INNER JOIN docente_responsable_taller ON docente_responsable_taller.id=clase.docente_responsable_taller_id
    #         INNER JOIN estudiante_taller ON estudiante_taller.docente_responsable_taller_id=docente_responsable_taller.id and docente_responsable_taller.ciclo_lectivo_taller_id=estudiante_taller.ciclo_lectivo_taller_id
    #         WHERE clase.id=%s
    #     """
    #     cursor.execute(sql, (data['clase_id']))
    #     clase = cursor.fetchone()
    #     sql2 = """
    #         INSERT INTO asistencia_estudiante_taller (estudiante_id, clase_id, fecha, docente_responsable_taller_id, ciclo_lectivo_id, presente)
    #         VALUES (%s, %s, %s, %s, %s, %s)
    #     """
    #     cursor.execute(sql2, (data['estudiante_id'], data['clase_id'], data['fecha'], clase['docente_responsable_taller_id'], clase['ciclo_lectivo_id'], '0'))
    #     cls.db.commit()
    #     return True
