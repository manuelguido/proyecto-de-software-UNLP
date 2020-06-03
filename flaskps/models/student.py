class Student(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT * FROM students
            INNER JOIN levels ON students.level_id = levels.level_id
            INNER JOIN genders ON students.gender_id = genders.gender_id
            INNER JOIN schools ON students.school_id = schools.school_id
            INNER JOIN neighborhoods ON students.neighborhood_id = neighborhoods.neighborhood_id
            INNER JOIN document_types ON students.document_type_id = document_types.document_type_id
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def all_reduced(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT students.student_id, students.name, students.lastname, students.document_number, document_types.name as document_type FROM students
            INNER JOIN levels ON students.level_id = levels.level_id
            INNER JOIN genders ON students.gender_id = genders.gender_id
            INNER JOIN schools ON students.school_id = schools.school_id
            INNER JOIN neighborhoods ON students.neighborhood_id = neighborhoods.neighborhood_id
            INNER JOIN document_types ON students.document_type_id = document_types.document_type_id
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, id_data):
        sql = """
            SELECT students.*,
                levels.name as level,
                genders.name as gender,
                schools.name as school,
                neighborhoods.name as neighborhood,
                document_types.name as document_type,
                responsables.name as responsable_name, responsables.lastname as responsable_lastname, responsables.phone as responsable_phone, responsables.responsable_type_id
            FROM students
            INNER JOIN levels ON students.level_id = levels.level_id
            INNER JOIN genders ON students.gender_id = genders.gender_id
            INNER JOIN schools ON students.school_id = schools.school_id
            INNER JOIN neighborhoods ON students.neighborhood_id = neighborhoods.neighborhood_id
            INNER JOIN document_types ON students.document_type_id = document_types.document_type_id
            INNER JOIN responsables ON students.responsable_id = responsables.responsable_id
            WHERE students.student_id=%s
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (id_data))
        return cursor.fetchone()

    # @classmethod
    # def allEstudianteTaller(cls):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT *, estudiante.nombre AS nombreestudiante, estudiante.apellido AS apellidoestudiante, docente.nombre AS nombredocente, docente.apellido AS apellidodocente, taller.nombre AS nombretaller FROM estudiante_taller
    #         INNER JOIN estudiante ON estudiante.id = estudiante_taller.estudiante_id
    #         INNER JOIN docente ON docente.id = estudiante_taller.docente_id
    #         INNER JOIN ciclo_lectivo_taller ON estudiante_taller.ciclo_lectivo_taller_id = ciclo_lectivo_taller.id
    #         INNER JOIN taller ON estudiante_taller.taller_id = taller.id
    #         INNER JOIN ciclo_lectivo ON estudiante_taller.ciclo_lectivo_id = ciclo_lectivo.id
    #     """
    #     cursor.execute(sql)
    #     return cursor.fetchall()

    # @classmethod
    # def allEstudianteTallerPaginated(cls,pagination,page):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT *, estudiante.nombre AS nombreestudiante, estudiante.apellido AS apellidoestudiante, docente.nombre AS nombredocente, docente.apellido AS apellidodocente, taller.nombre AS nombretaller FROM estudiante_taller
    #         INNER JOIN estudiante ON estudiante.id = estudiante_taller.estudiante_id
    #         INNER JOIN docente ON docente.id = estudiante_taller.docente_id
    #         INNER JOIN ciclo_lectivo_taller ON estudiante_taller.ciclo_lectivo_taller_id = ciclo_lectivo_taller.id
    #         INNER JOIN taller ON estudiante_taller.taller_id = taller.id
    #         INNER JOIN ciclo_lectivo ON estudiante_taller.ciclo_lectivo_id = ciclo_lectivo.id
    #         LIMIT {limit} offset {offset}
    #     """
    #     cursor.execute(sql.format(limit = pagination, offset = (pagination * int(page - 1)) ))
    #     return cursor.fetchall()

    # @classmethod
    # def searchByFirstName(cls,firstname):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT  * , nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio  FROM estudiante
    #         INNER JOIN nivel ON estudiante.nivel_id = nivel.id
    #         INNER JOIN genero ON estudiante.genero_id = genero.id
    #         INNER JOIN escuela ON estudiante.escuela_id = escuela.id
    #         INNER JOIN barrio ON estudiante.barrio_id = barrio.id
    #         WHERE estudiante.nombre LIKE '%{firstname}%'
    #     """
    #     cursor.execute(sql.format(firstname = firstname))
    #     return cursor.fetchall()

    # @classmethod
    # def searchByLastName(cls,lastname):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT  * , nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio  FROM estudiante
    #         INNER JOIN nivel ON estudiante.nivel_id = nivel.id
    #         INNER JOIN genero ON estudiante.genero_id = genero.id
    #         INNER JOIN escuela ON estudiante.escuela_id = escuela.id
    #         INNER JOIN barrio ON estudiante.barrio_id = barrio.id
    #         WHERE estudiante.apellido LIKE '%{lastname}%'
    #     """
    #     cursor.execute(sql.format(lastname = lastname))
    #     return cursor.fetchall()
    
    # @classmethod
    # def searchByBoth(cls,firstname,lastname):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT  * , nivel.nombre as nivel, genero.nombre as genero, escuela.nombre as escuela, barrio.nombre as barrio  FROM estudiante
    #         INNER JOIN nivel ON estudiante.nivel_id = nivel.id
    #         INNER JOIN genero ON estudiante.genero_id = genero.id
    #         INNER JOIN escuela ON estudiante.escuela_id = escuela.id
    #         INNER JOIN barrio ON estudiante.barrio_id = barrio.id
    #         WHERE estudiante.nombre LIKE '%{firstname}%' AND estudiante.apellido LIKE '%{lastname}%'
    #     """
    #     cursor.execute(sql.format(firstname = firstname, lastname = lastname))
    #     return cursor.fetchall()

    # @classmethod
    # def getLastPage(cls,pagination,page):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT  * FROM estudiante
    #         COUNT
    #     """
    #     if ((cursor.execute(sql) / pagination) <= page):
    #         return 1
    #     else:
    #         return 0

    # @classmethod
    # def getLastPageTaller(cls,pagination,page):
    #     cursor = cls.db.cursor()
    #     sql = """
    #         SELECT * FROM estudiante_taller
    #         COUNT
    #     """
    #     if ((cursor.execute(sql) / pagination) <= page):
    #         return 1
    #     else:
    #         return 0

    @classmethod
    def create(cls, data, responsable_id):
        sql = """
            INSERT INTO students (lastname, name, birth_date, neighborhood_id, level_id, address, gender_id, school_id, document_type_id, document_number, phone, location_id, responsable_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor = cls.db.cursor()
        cursor.execute(sql, (data['lastname'], data['name'], data['birth_date'], data['neighborhood_id'], data['level_id'], data['address'], data['gender_id'], data['school_id'], data['document_type_id'], data['document_number'], data['phone'], data['location_id'], responsable_id))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, data):
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE students
               SET lastname=%s, name=%s, birth_date=%s, neighborhood_id=%s, level_id=%s, address=%s, gender_id=%s, school_id=%s, document_type_id=%s, document_number=%s, phone=%s, location_id=%s
               WHERE student_id=%s
            """, (data['lastname'], data['name'], data['birth_date'], data['neighborhood_id'], data['level_id'], data['address'], data['gender_id'], data['school_id'], data['document_type_id'], data['document_number'], data['phone'], data['location_id'], data['student_id']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, id_data):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM students WHERE student_id=%s", (id_data))
        cls.db.commit()
        return True

    # @classmethod
    # def estudianteNoEnTaller(cls, data):
    #     cursor = cls.db.cursor() 
    #     sql = """
    #            SELECT *
    #            FROM estudiante_taller
    #            WHERE estudiante_taller.estudiante_id=%s and estudiante_taller.docente_responsable_taller_id=%s
    #         """
    #     a = cursor.execute(sql, (data['estudiante_id'], data['docente_responsable_taller_id']))
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
    # def findByClass(cls, id_data):
    #     sql = """
    #         SELECT *, clase.id AS clase_id FROM estudiante
    #         INNER JOIN estudiante_taller ON estudiante_taller.estudiante_id=estudiante.id
    #         INNER JOIN docente_responsable_taller ON estudiante_taller.docente_responsable_taller_id=docente_responsable_taller.id
    #         INNER JOIN clase ON clase.docente_responsable_taller_id=docente_responsable_taller.id
    #         WHERE clase.id=%s
    #     """
    #     cursor = cls.db.cursor()
    #     cursor.execute(sql, (id_data))
    #     return cursor.fetchall()
        
