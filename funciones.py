import mysql.connector


RESET = '\033[0m'
VERDE = '\033[92m'
ROJO = '\033[91m'
AZUL = '\033[94m'
AMARILLO = '\033[93m'
CYAN = '\033[96m'

def borrarPantalla():
    print("\033c") 

def espereTecla():
    input(f"\n{AMARILLO}...|Oprime cualquier tecla para continuar|...{RESET}")

def accionExitosa():
    print(f"\n{VERDE}✅ ...|Accion Realizada con Exito|...{RESET}")

def accionNoExitosa():
    print(f"\n{ROJO}❌ ...|No fue posible realizar esta Accion, intentalo nuevamente|...{RESET}")

def terminarSistema():
    print(f"\n{CYAN}👋 ...::::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, VUELVE PRONTO :::::...{RESET}")

def opcionInvalida():
    print(f"\n{ROJO}⚠️ \t...|Opcion Invalida, vuelve a intentarlo|... {RESET}")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_personal"
        )
        return conexion
    except:
        borrarPantalla()
        print(f"{ROJO}...|Por el momento no es posible establecer una comunicacion con la base de datos|...{RESET}")
        return None

def conectar_n():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_nomina"
        )
        return conexion
    except:
        borrarPantalla()
        print(f"{ROJO}...|Por el momento no es posible establecer una comunicacion con la base de datos|...{RESET}")
        return None 