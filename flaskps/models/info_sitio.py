from sqlalchemy import text
from flaskps.db import get_db

class InfoSitio(object):

    #retorna el estado del sitio 1 = activo, 0 = inactivo
    def index():
        connection = get_db()
        sql_select_Query = "select * from info_sitio"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        results = cursor.fetchall()        
        for r in results:
            y = r['activo']
            break
        return y