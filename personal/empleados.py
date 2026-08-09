import re
from personal import crud
import funciones

def menuSecundario():
    print(f"{funciones.CYAN}\n\t\t...::: 👤 M E N U  E M P L E A D O S :::...{funciones.RESET}\n")
    print("\t1.- ➕ Agregar")
    print("\t2.- 🗑️  Borrar")
    print("\t3.- ✏️  Modificar")
    print("\t4.- 📋 Mostrar")
    print("\t5.- 🔍 Buscar")
    print("\t6.- 🧹 Limpiar")
    print("\t7.- ⬅️  Salir\n")
    opcion = input("\t👉 Escribe una opción: ").strip()
    return opcion

def validarRFC(rfc):
    patron = r'^[A-Z]{4}\d{6}[A-Z0-9]{3}$'
    if re.match(patron, rfc):
        return True
    return False

def agregarPersonal(conexionBD):
    print("\n\t\t...::: AGREGAR PERSONAL :::...\n")
    nombre = input("Ingresa el nombre: ").upper().strip()
    rfc = input("Ingresa el RFC (13 caracteres): ").upper().strip()
    
    if validarRFC(rfc):
        puesto = input("Ingresa el puesto: ").upper().strip()
        datos = (nombre, rfc, puesto) 
        
        respuesta = crud.insertar(datos, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        print("\n\t[!] Error: El formato del RFC es incorrecto.")
    
    funciones.espereTecla()

def mostrarPersonal(conexionBD):
    print("\n\t\t...::: MOSTRAR PERSONAL :::...\n")
    registros = crud.consultar(conexionBD)
    
    if len(registros) > 0:
        lista_personal = []
        for fila in registros:
            diccionario = {"id": fila[0], "nombre": fila[1], "rfc": fila[2], "puesto": fila[3]}
            lista_personal.append(diccionario)
            
        print(f"{'ID':<5} {'NOMBRE':<20} {'RFC':<18} {'PUESTO':<20}")
        print("-" * 65)
        
        try:
            archivo = open("reporte_personal.txt", "w")
            archivo.write("----- REPORTE DE PERSONAL -----\n")
            for emp in lista_personal:
                texto = f"{emp['id']:<5} {emp['nombre']:<20} {emp['rfc']:<18} {emp['puesto']:<20}"
                print(texto)
                archivo.write(texto + "\n")
            archivo.close()
            print("\n\t(Reporte 'reporte_personal.txt' generado exitosamente)")
        except:
            print("\n\t(Error al generar reporte txt)")
            
    else:
        print("\n... No hay personal registrado para mostrar ...")
        
    funciones.espereTecla()

def borrarPersonal(conexionBD):
    print("\n\t\t...::: BORRAR PERSONAL :::...\n")
    rfc = input("Ingresa el RFC del empleado a borrar: ").upper().strip()
    
    existe = crud.buscar(rfc, conexionBD)
    if len(existe) > 0:
        respuesta = crud.borrar(rfc, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        print("\n\t... El empleado con ese RFC no existe ...")
        
    funciones.espereTecla()

def modificarPersonal(conexionBD):
    print("\n\t\t...::: MODIFICAR PERSONAL :::...\n")
    rfc = input("Ingresa el RFC del empleado a modificar: ").upper().strip()
    
    existe = crud.buscar(rfc, conexionBD)
    if len(existe) > 0:
        nuevo_nombre = input("Escribe el nuevo nombre: ").upper().strip()
        nuevo_puesto = input("Escribe el nuevo puesto: ").upper().strip()
        
        nuevos_datos = (nuevo_nombre, nuevo_puesto, rfc)
        
        respuesta = crud.modificar(rfc, nuevos_datos, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        print("\n\t... El empleado con ese RFC no existe ...")
        
    funciones.espereTecla()

def buscarPersonal(conexionBD):
    print("\n\t\t...::: BUSCAR PERSONAL :::...\n")
    rfc = input("Ingresa el RFC a buscar: ").upper().strip()
    
    registros = crud.buscar(rfc, conexionBD)
    if len(registros) > 0:
        print("\n\tEmpleado encontrado:")
        print(f"ID: {registros[0][0]}\nNombre: {registros[0][1]}\nRFC: {registros[0][2]}\nPuesto: {registros[0][3]}")
    else:
        print("\n\t... El empleado con ese RFC no existe ...")
        
    funciones.espereTecla()

def limpiarPersonal(conexionBD):
    print("\n\t\t...::: LIMPIAR PERSONAL :::...\n")
    seguro = input("¿Estás seguro de borrar TODO el personal? (Si/No): ").lower().strip()
    if seguro == "si":
        respuesta = crud.vaciar(conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        print("\n\t... Operación cancelada ...")
        
    funciones.espereTecla()