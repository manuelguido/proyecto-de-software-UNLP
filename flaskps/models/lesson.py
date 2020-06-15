class Lesson(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT lessons.lesson_id, cycles.year, levels.name AS level, semesters.name AS semester, workshops.name AS workshop, workshop_types.name AS workshop_type
            FROM lessons
            INNER JOIN cycle_workshop ON cycle_workshop.cycle_workshop_id = lessons.cycle_workshop_id
            INNER JOIN cycles ON cycles.cycle_id = cycle_workshop.cycle_id
            INNER JOIN workshops ON workshops.workshop_id = cycle_workshop.workshop_id
            INNER JOIN workshop_types ON workshop_types.workshop_type_id = lessons.workshop_type_id
            INNER JOIN semesters ON semesters.semester_id = cycles.semester_id
            INNER JOIN levels ON levels.level_id = lessons.level_id
            ORDER BY cycles.year DESC, semesters.name DESC
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT lessons.lesson_id, lessons.cycle_workshop_id, lessons.workshop_type_id, lessons.level_id, cycles.year, levels.name AS level, semesters.name AS semester, workshops.name AS workshop, workshop_types.name AS workshop_type
            FROM lessons
            INNER JOIN cycle_workshop ON cycle_workshop.cycle_workshop_id = lessons.cycle_workshop_id
            INNER JOIN cycles ON cycles.cycle_id = cycle_workshop.cycle_id
            INNER JOIN workshops ON workshops.workshop_id = cycle_workshop.workshop_id
            INNER JOIN workshop_types ON workshop_types.workshop_type_id = lessons.workshop_type_id
            INNER JOIN semesters ON semesters.semester_id = cycles.semester_id
            INNER JOIN levels ON levels.level_id = lessons.level_id
            WHERE lessons.lesson_id=%s"""
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    @classmethod
    def create(cls, lesson):
        cursor = cls.db.cursor()
        sql = "INSERT INTO lessons (cycle_workshop_id, workshop_type_id, level_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (lesson['cycle_workshop_id'], lesson['workshop_type_id'], lesson['level_id']))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, lesson):
        cursor = cls.db.cursor()
        sql= "UPDATE lessons SET cycle_workshop_id=%s, workshop_type_id=%s, level_id=%s WHERE lesson_id=%s"
        cursor.execute(sql, (lesson['cycle_workshop_id'], lesson['workshop_type_id'], lesson['level_id'], lesson['lesson_id']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, lesson_id):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM lessons WHERE lesson_id=%s", (lesson_id))
        cls.db.commit()
        return True

    @classmethod
    def lesson_exists(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT lessons.lesson_id COUNT
            FROM lessons
            WHERE lessons.cycle_workshop_id=%s and lessons.workshop_type_id=%s and lessons.level_id=%s
        """
        result = cursor.execute(sql, (data['cycle_workshop_id'], data['workshop_type_id'], data['level_id']))
        cls.db.commit()
        return (result > 0)

    @classmethod
    def lesson_exists_not_self(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT lessons.lesson_id COUNT
            FROM lessons
            WHERE lessons.cycle_workshop_id=%s and lessons.workshop_type_id=%s and lessons.level_id=%s and lessons.lesson_id<>%s
        """
        result = cursor.execute(sql, (data['cycle_workshop_id'], data['workshop_type_id'], data['level_id'], data['lesson_id']))
        cls.db.commit()
        return (result > 0)

    @classmethod
    def has_student(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT lesson_student.lesson_id COUNT
            FROM lesson_student
            WHERE lesson_id=%s and student_id=%s
        """
        result = cursor.execute(sql, (data['lesson_id'], data['student_id']))
        cls.db.commit()
        return (result > 0)

    @classmethod
    def add_student(cls, data):
        cursor = cls.db.cursor()
        sql = "INSERT INTO lesson_student (lesson_id, student_id) VALUES (%s, %s)"
        cursor.execute(sql, (data['lesson_id'], data['student_id']))
        cls.db.commit()
        return True

    @classmethod
    def remove_student(cls, data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM lesson_student WHERE lesson_id=%s and student_id=%s", (data['lesson_id'], data['student_id']))
        cls.db.commit()
        return True

    @classmethod
    def students(cls, lesson_id):
        cursor = cls.db.cursor()
        sql = """
            SELECT DISTINCT students.student_id, students.name, students.lastname, students.document_number, document_types.name as document_type FROM students
            INNER JOIN document_types ON students.document_type_id = document_types.document_type_id
            INNER JOIN lesson_student ON students.student_id = lesson_student.student_id
            WHERE lesson_student.lesson_id=%s
        """
        cursor.execute(sql, (lesson_id))
        return cursor.fetchall()

    @classmethod
    def students_for_assistance(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT DISTINCT students.student_id, students.name, students.lastname, students.document_number, document_types.name as document_type FROM students
            INNER JOIN document_types ON students.document_type_id = document_types.document_type_id
            INNER JOIN lesson_student ON students.student_id = lesson_student.student_id
            WHERE lesson_student.lesson_id=%s
            AND students.student_id NOT IN (
                SELECT student_id
                FROM assistances
                INNER JOIN schedules ON assistances.schedule_id = schedules.schedule_id
                WHERE schedules.lesson_id = %s and schedules.schedule_id = %s and assistances.date = %s
            )
        """
        cursor.execute(sql, (data['lesson_id'], data['lesson_id'], data['schedule_id'], data['date']))
        return cursor.fetchall()
