from flaskps.db import get_db

class InfoSitio(object):

    db = None

    #retorna el estado del sitio 1 = activo, 0 = inactivo
    @classmethod
    def index(cls):
        connection = get_db()
        sql_select_Query = "select * from configuracion"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        results = cursor.fetchall()        
        for r in results:
            y = r['activo']
            break
        return y

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM configuracion'
        cursor = cls.db.cursor()
        cursor.execute(sql)

        return cursor.fetchall()


    @classmethod
    def change_site_status(cls, request):
        estado = request['estado_sitio']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE configuracion
               SET activo=%s
               WHERE id=1
            """, (estado))
        cls.db.commit()

        return True

    @classmethod
    def change_site_pagination(cls, request):
        estado = request['paginacion']
        cursor = cls.db.cursor()
        cursor.execute("""
               UPDATE configuracion
               SET paginacion=%s
               WHERE id=1
            """, (estado))
        cls.db.commit()

        return True