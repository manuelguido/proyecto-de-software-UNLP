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