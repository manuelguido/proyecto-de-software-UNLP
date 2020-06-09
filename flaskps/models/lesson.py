class Lesson(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM lessons")
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM lessons WHERE lessons.lesson_id=%s"
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
        cursor.execute(sql, (lesson['cycle_workshop_id'], lesson['workshop_type_id'], lesson['level_id']))
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
