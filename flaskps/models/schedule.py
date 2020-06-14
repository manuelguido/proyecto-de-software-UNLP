class Schedule(object):

    db = None

    @classmethod
    def all(cls, lesson_id):
        cursor = cls.db.cursor()
        sql = """
            SELECT schedules.*, cores.name AS core, days.name AS day
            FROM schedules
            INNER JOIN days ON days.day_id = schedules.day_id
            INNER JOIN cores ON cores.core_id = schedules.day_id
            WHERE schedules.lesson_id = %s
        """
        cursor.execute(sql, (lesson_id))
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM schedules WHERE schedules.schedule_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    @classmethod
    def add(cls, schedule):
        cursor = cls.db.cursor()
        sql = "INSERT INTO schedules (lesson_id, core_id, day_id, hour_from, hour_to) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (schedule['lesson_id'], schedule['core_id'], schedule['day_id'], schedule['hour_from'], schedule['hour_to']))
        cls.db.commit()

        sql = """
            SELECT schedules.*, cores.name AS core, days.name AS day
            FROM schedules
            INNER JOIN days ON days.day_id = schedules.day_id
            INNER JOIN cores ON cores.core_id = schedules.day_id
            WHERE schedules.lesson_id=%s and schedules.core_id=%s and schedules.day_id=%s and schedules.hour_from=%s and schedules.hour_to=%s
            """
        cursor.execute(sql, (schedule['lesson_id'], schedule['core_id'], schedule['day_id'], schedule['hour_from'], schedule['hour_to']))
        return cursor.fetchone()

    @classmethod
    def remove(cls, schedule_id):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM schedules WHERE schedule_id=%s", (schedule_id))
        cls.db.commit()
        return True

    @classmethod
    def schedule_exists(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT schedules.schedule_id COUNT
            FROM schedules
            WHERE schedules.lesson_id=%s and schedules.core_id=%s and schedules.day_id=%s and schedules.hour_from=%s and schedules.hour_to=%s
        """
        result = cursor.execute(sql, (data['lesson_id'], data['core_id'], data['day_id'], data['hour_from'], data['hour_to']))
        cls.db.commit()
        return (result > 0)

    @classmethod
    def schedule_exists_not_self(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT schedules.schedule_id COUNT
            FROM schedules
            WHERE schedules.lesson_id=%s and schedules.core_id=%s and schedules.day_id=%s and schedules.hour_from=%s and schedules.hour_to=%s and schedules.schedule_id<>%s
        """
        result = cursor.execute(sql, (data['lesson_id'], data['core_id'], data['day_id'], data['hour_from'], data['hour_to'], data['schedule_id']))
        cls.db.commit()
        return (result > 0)
