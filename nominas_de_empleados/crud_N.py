

def insertar(datos, conexionBD):
    try:
        cursor = conexionBD.cursor()
        sql = "INSERT INTO nomina (nombre, sueldo, pago) VALUES (%s, %s, %s)"
        cursor.execute(sql, datos)
        conexionBD.commit()
        return True
    except Exception as e:
        # Esta línea imprimirá el error real en color rojo para que lo podamos ver
        print(f"\n\033[91m[!] Error de base de datos: {e}\033[0m")
        return False

def consultar(conexionBDN):
    try:
        cursor = conexionBDN.cursor()
        cursor.execute("SELECT * FROM nomina")
        return cursor.fetchall()
    except:
        return []

def buscar(nombre, conexionBDN):
    try:
        cursor = conexionBDN.cursor()
        sql = "SELECT * FROM nomina WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        return cursor.fetchall()
    except:
        return []

def borrar(nombre, conexionBDN):
    try:
        cursor = conexionBDN.cursor()
        sql = "DELETE FROM nomina WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        conexionBDN.commit()
        cursor.close()
        return True
    except:
        return False

def modificar(nuevos_datos, conexionBD):
    try:
        cursor = conexionBD.cursor()
        sql = "UPDATE nomina SET sueldo = %s, pago = %s WHERE nombre = %s"
        cursor.execute(sql, nuevos_datos)
        conexionBD.commit()
        cursor.close()
        return True
    except :
        return False

def vaciar(conexionBDN):
    try:
        cursor = conexionBDN.cursor()
        cursor.execute("DELETE FROM nomina")
        cursor.execute("ALTER TABLE nomina AUTO_INCREMENT = 1")
        conexionBDN.commit()
        return True
    except:
        return False