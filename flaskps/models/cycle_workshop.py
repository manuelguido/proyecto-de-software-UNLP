class CycleWorkshop(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, semesters.name AS semester FROM workshops
            INNER JOIN cycle_workshop ON cycle_workshop.workshop_id = workshops.workshop_id
            INNER JOIN cycles ON cycles.cycle_id = cycle_workshop.cycle_id
            INNER JOIN semesters ON semesters.semester_id = cycles.semester_id
            ORDER BY year DESC
            """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            SELECT *, semesters.name AS semester FROM workshops
            INNER JOIN cycle_workshop ON cycle_workshop.workshop_id = workshops.workshop_id
            INNER JOIN cycles ON cycles.cycle_id = cycle_workshop.cycle_id
            INNER JOIN semesters ON semesters.semester_id = cycles.semester_id
            WHERE cycle_workshop_id=%s
            """
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    @classmethod
    def get_by_ids(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM cycle_workshop WHERE
            workshop_id=%s and cycle_id=%s
            """
        cursor.execute(sql, (data['workshop_id'], data['cycle_id']))
        return cursor.fetchone()

    @classmethod
    def cycle_workshop_exists(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT cycle_workshop.cycle_workshop_id COUNT
            FROM cycle_workshop
            WHERE workshop_id=%s and cycle_id=%s
        """
        result = cursor.execute(sql, (data['workshop_id'], data['cycle_id']))
        cls.db.commit()
        return (result > 0)

    @classmethod
    def create(cls, data):
        cursor = cls.db.cursor()
        sql = "INSERT INTO cycle_workshop (workshop_id, cycle_id) VALUES (%s, %s)"
        cursor.execute(sql, (data['workshop_id'], data['cycle_id']))
        cls.db.commit()

        sql = """
            SELECT *, semesters.name AS semester FROM workshops
            INNER JOIN cycle_workshop ON cycle_workshop.workshop_id = workshops.workshop_id
            INNER JOIN cycles ON cycles.cycle_id = cycle_workshop.cycle_id
            INNER JOIN semesters ON semesters.semester_id = cycles.semester_id
            WHERE cycle_workshop.workshop_id=%s and cycle_workshop.cycle_id=%s
            ORDER BY year DESC
            """
        cursor.execute(sql, (data['workshop_id'], data['cycle_id']))
        return cursor.fetchone()

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        sql = """
            DELETE FROM cycle_workshop
            WHERE cycle_workshop_id=%s
        """
        cursor.execute(sql, (id_data))
        cls.db.commit()
        return True