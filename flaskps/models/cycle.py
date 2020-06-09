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
    def create(cls, cycle):
        cursor = cls.db.cursor()
        sql = "INSERT INTO cycles (semester_id, year, date_from, date_to) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (cycle['semester_id'], cycle['year'], cycle['date_from'], cycle['date_to']))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, cycle):
        cursor = cls.db.cursor()
        sql= "UPDATE cycles SET semester_id=%s, year=%s, date_from=%s, date_to=%s WHERE cycle_id=%s"
        cursor.execute(sql, (cycle['semester_id'], cycle['year'], cycle['date_from'], cycle['date_to'], cycle['cycle_id']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, cycle_id):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM cycles WHERE cycle_id=%s", (cycle_id))
        cls.db.commit()
        return True

    @classmethod
    def semester_exists(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT cycles.cycle_id COUNT
            FROM cycles
            WHERE cycles.semester_id=%s and cycle.year=%s
        """
        result = cursor.execute(sql, (data['semester_id'], data['year']))
        cls.db.commit()
        return (result > 0)

    @classmethod
    def semester_exists_not_self(cls, data):
        cursor = cls.db.cursor()
        sql = """
            SELECT cycles.cycle_id COUNT
            FROM cycles
            WHERE cycles.semester_id=%s and cycle.year=%s and cycle.cycle_id<>%s
        """
        result = cursor.execute(sql, (data['semester_id'], data['year'], data['cycle_id']))
        cls.db.commit()
        return (result > 0)

    # @classmethod
    # def cicloNoTieneTaller(cls, data):
    #     cursor = cls.db.cursor() 
    #     sql = """
    #            SELECT taller.id
    #            FROM taller
    #            WHERE id=%s
    #         """
    #     cursor.execute(sql, (data['taller_id']))
    #     taller_id = cursor.fetchone()
    #     sql2 = """
    #            SELECT ciclo_lectivo.id
    #            FROM ciclo_lectivo
    #            WHERE id=%s
    #         """
    #     cursor.execute(sql2, (data['ciclo_lectivo_id']))
    #     ciclo_lectivo_id = cursor.fetchone()
    #     cursor = cls.db.cursor()
    #     sql = """
    #            SELECT ciclo_lectivo_taller.taller_id COUNT
    #            FROM ciclo_lectivo_taller
    #            WHERE taller_id=%s and ciclo_lectivo_id=%s
    #         """
    #     a = cursor.execute(sql, (taller_id['id'], ciclo_lectivo_id['id']))
    #     cls.db.commit()
    #     if (a>0):
    #         return False
    #     else:
    #         return True
