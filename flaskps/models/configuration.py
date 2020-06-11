class Configuration(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        cursor.execute("SELECT  * FROM configuration")
        return cursor.fetchall()

    # @classmethod
    # def change_site_status(cls, estado_sitio):
    #     cursor = cls.db.cursor()
    #     cursor.execute("""
    #            UPDATE configuracion
    #            SET activo=%s
    #            WHERE id=1
    #         """, (estado_sitio))
    #     cls.db.commit()

    #     return True

    @classmethod
    def update(cls, data):
        cursor = cls.db.cursor()
        sql = """
               UPDATE configuration
               SET active=%s, title=%s, description=%s, email=%s
            """
        cursor.execute(sql, (data['active'], data['title'], data['description'], data['email']))
        cls.db.commit()
        return True

    # @classmethod
    # def change_site_pagination(cls, paginacion):
    #     cursor = cls.db.cursor()
    #     cursor.execute("""
    #            UPDATE configuracion
    #            SET paginacion=%s
    #            WHERE id=1
    #         """, (paginacion))
    #     cls.db.commit()
        
    #     return True

    # @classmethod
    # def get_pagination(cls):
    #     cursor = cls.db.cursor()
    #     cursor.execute("select * from configuracion")
    #     results = cursor.fetchall()        
    #     for r in results:
    #         paginacion = r['paginacion']
    #         break
    #     return paginacion
