def insertar(datos, conexionBD):
    try:
        cursor = conexionBD.cursor()
        sql = "INSERT INTO personal (nombre, rfc, puesto) VALUES (%s, %s, %s)"
        cursor.execute(sql, datos)
        conexionBD.commit()
        return True
    except:
        return False

def consultar(conexionBD):
    try:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM personal")
        return cursor.fetchall()
    except:
        return []

def buscar(rfc_buscar, conexionBD):
    try:
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM personal WHERE rfc = %s"
        cursor.execute(sql, (rfc_buscar,))
        return cursor.fetchall()
    except:
        return []

def borrar(rfc_borrar, conexionBD):
    try:
        cursor = conexionBD.cursor()
        sql = "DELETE FROM personal WHERE rfc = %s"
        cursor.execute(sql, (rfc_borrar,))
        conexionBD.commit()
        return True
    except:
        return False

def modificar(rfc_actual, nuevos_datos, conexionBD):
    try:
        cursor = conexionBD.cursor()
        sql = "UPDATE personal SET nombre = %s, puesto = %s WHERE rfc = %s"
        cursor.execute(sql, nuevos_datos)
        conexionBD.commit()
        return True
    except:
        return False

def vaciar(conexionBD):
    try:
        cursor = conexionBD.cursor()
        cursor.execute("DELETE FROM personal")
        cursor.execute("ALTER TABLE personal AUTO_INCREMENT = 1") 
        conexionBD.commit()
        return True
    except:
        return False