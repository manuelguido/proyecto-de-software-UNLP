class Student(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM students")
        data = cursor.fetchall()
        return data

    @classmethod
    def store(cls, data):
        sql = """
            INSERT INTO students (name, lastname, email, phone, level, dni, address, neighborhood, pmt_name, instrument, birth_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, list(data.values()))
        cls.db.commit()

        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s", (id_data,))
        cls.db.commit()

        return True

    @classmethod
    def update(cls, request):
        id_data = request.form['id']
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        level = request.form['level']
        dni = request.form['dni']
        address = request.form['address']
        neighborhood = request.form['neighborhood']
        pmt_name = request.form['pmt_name']
        instrument = request.form['instrument']
        birth_date = request.form['birth_date']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE students
               SET name=%s, lastname=%s, email=%s, phone=%s, level=%s, dni=%s, address=%s, neighborhood=%s, pmt_name=%s, instrument=%s, birth_date=%s
               WHERE id=%s
            """, (name, lastname, email, phone, level, dni, address, neighborhood, pmt_name, instrument, birth_date, id_data))
        cls.db.commit()

        return True
    





    @classmethod
    def find_by_email_and_pass(cls, email, password):
        sql = """
            SELECT * FROM users AS u
            WHERE u.email = %s AND u.password = %s
        """

        cursor = cls.db.cursor()
        cursor.execute(sql, (email, password))

        return cursor.fetchone()
