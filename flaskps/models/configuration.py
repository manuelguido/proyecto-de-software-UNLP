class Configuration(object):

    db = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM configuracion'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchone()


    @classmethod
    def change_site_status(cls, estado_sitio):
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE configuracion
               SET activo=%s
               WHERE id=1
            """, (estado_sitio))
        cls.db.commit()

        return True

    @classmethod
    def update_info_sitio(cls, request):
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE configuracion
               SET titulo=%s, descripcion=%s, email=%s
               WHERE id=1
            """, (request['titulo'], request['descripcion'], request['email']))
        cls.db.commit()

        return True

    @classmethod
    def change_site_pagination(cls, paginacion):
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE configuracion
               SET paginacion=%s
               WHERE id=1
            """, (paginacion))
        cls.db.commit()
        
        return True

    @classmethod
    def get_pagination(cls):
        cursor = cls.db.cursor()
        cursor.execute("select * from configuracion")
        results = cursor.fetchall()        
        for r in results:
            paginacion = r['paginacion']
            break
        return paginacion
