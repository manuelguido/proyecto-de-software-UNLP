class Lesson(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM lessons")
        data = cursor.fetchall()
        return data

    @classmethod
    def get(cls, id_data):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM lessons WHERE lessons.lesson_id=%s"
        cursor.execute(sql, (id_data))
        return cursor.fetchone()
