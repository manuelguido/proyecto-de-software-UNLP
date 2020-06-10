class Workshop(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = 'SELECT * FROM workshops'
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, workshop_id):
        cursor = cls.db.cursor()
        sql = "SELECT * FROM workshops WHERE workshop_id=%s"
        cursor.execute(sql, (workshop_id))
        return cursor.fetchone()

    @classmethod
    def create(cls, cycle):
        cursor = cls.db.cursor()
        sql = "INSERT INTO workshops (name, short_name) VALUES (%s, %s)"
        cursor.execute(sql, (cycle['name'], cycle['short_name']))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, workshop):
        cursor = cls.db.cursor()
        sql= "UPDATE workshops SET name=%s, short_name=%s WHERE workshop_id=%s"
        cursor.execute(sql, (workshop['name'], workshop['short_name'], workshop['workshop_id']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, workshop_id):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM workshops WHERE workshop_id=%s", (workshop_id))
        cls.db.commit()
        return True

    @classmethod
    def workshop_exists(cls, workshop):
        cursor = cls.db.cursor()
        sql = """
            SELECT workshops.workshop_id COUNT
            FROM workshops
            WHERE workshops.name=%s and workshops.short_name=%s
        """
        result = cursor.execute(sql, (workshop['name'], workshop['short_name']))
        cls.db.commit()
        return (result > 0)

    @classmethod
    def workshop_exists_not_self(cls, workshop):
        cursor = cls.db.cursor()
        sql = """
            SELECT workshops.workshop_id COUNT
            FROM workshops
            WHERE workshops.name=%s and workshops.short_name=%s and workshops.workshop_id<>%s
        """
        result = cursor.execute(sql, (workshop['name'], workshop['short_name'], workshop['workshop_id']))
        cls.db.commit()
        return (result > 0)
