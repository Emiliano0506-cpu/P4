import funciones 
from nominas_de_empleados import crud_N

def menuNomina():
    print(f"{funciones.AZUL}\n\t\t...:::💰 M E N U  N O M I N A  :::...{funciones.RESET}\n")
    print("\t1.- ➕ Insertar\n\t2.- 🗑️  Eliminar\n\t3.- ✏️  Actualizar\n\t4.- 📋 Mostrar\n\t5.- 🔍 Buscar\n\t6.- 🧹 Vaciar\n\t7.- ⬅️  Regresar\n")
    opcion_n = input("\t👉 Escribe una opcion: ").strip()
    return opcion_n


def agregarNomina(conexionBDN):
    print(f"{funciones.CYAN}\n\t...::: ➕ INSERTAR NOMINA DEL PERSONAL :::...{funciones.RESET}\n")
    nombre = input("Ingresa el nombre:... ").upper().strip()
    sueldo= float(input("Ingresa tu sueldo por dia:..."))
    dias=int(input("Ingrese la cantidad de dias completos trabajados:..."))
    pago=dias*sueldo
    datos = (nombre, sueldo,pago)
    respuesta = crud_N.insertar(datos, conexionBDN)
    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNoExitosa()
    funciones.espereTecla()
    


def mostrarNomina(conexionBDN):
    print(f"{funciones.CYAN}\n\t...::: 📄 CONSULTAR NOMINA DEL PERSONAL :::...{funciones.RESET}\n")
    registros = crud_N.consultar(conexionBDN)
    if len(registros) > 0:
        lista_personal = []
        for fila in registros:
            diccionario = {"id": fila[0], "nombre": fila[1], "sueldo": fila[2], "pago": fila[3]}
            lista_personal.append(diccionario)

        print(f"{funciones.AMARILLO}{'ID':<5} | {'NOMBRE':<15} | {'SUELDO':<10} | {'PAGO':<10}{funciones.RESET}")
        print("-" * 70)
        for empleado in lista_personal:
            print(f"{empleado['id']:<5} | {empleado['nombre']:<15} | {empleado['sueldo']:<10} | {empleado['pago']:<10}")
        print("-" * 70)
    else:
        print(f"{funciones.AMARILLO}\n⚠ ... No hay empleados registrados ...{funciones.RESET}\n")

    funciones.espereTecla()

def borrarNomina(conexionBDN):
    print(f"{funciones.CYAN}\n\t...::: 🗑️  ELIMINAR NOMINA DEL PERSONAL  :::...{funciones.RESET}\n")
    nombre = input("Ingresa el nombre del empleado a elimiar:...  ").upper().strip()
    existe = crud_N.buscar(nombre, conexionBDN)
    if len(existe) > 0:
        respuesta = crud_N.borrar(nombre, conexionBDN)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        print(f"{funciones.AMARILLO}\n⚠ ... El empleado con ese nombre no existe ...{funciones.RESET}\n")
    funciones.espereTecla()

def modificarNomina(conexionBDN):
    print(f"{funciones.CYAN}\n\t...::: ✏️  ACTUALIZAR NOMINA DEL PERSONAL :::...{funciones.RESET}\n")
    nombre = input("Ingresa el nombre del empleado a Actualizar: ").upper().strip()
    
    existe = crud_N.buscar(nombre, conexionBDN)
    if len(existe) > 0:
        try:
            nuevo_sueldo = float(input("Escribe el nuevo sueldo diario:$..."))
            dias=int(input("Ingrese los dias trabajados:...."))
            nuevo_sueldoFinal=dias*nuevo_sueldo
            nuevos_datos = (nuevo_sueldo, nuevo_sueldoFinal, nombre)
            
            respuesta = crud_N.modificar( nuevos_datos, conexionBDN)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
        except ValueError:
            print(f"{funciones.ROJO}\n⚠️ |Error|: El sueldo debe ser un numero.{funciones.RESET}")
    else:
        print(f"{funciones.AMARILLO}\n⚠ ... El empleado con ese nombre no existe ...{funciones.RESET}\n")
    funciones.espereTecla()

def buscarNomina(conexionBDN):
    print(f"{funciones.CYAN}\n\t...::: 🔍 BUSCAR NOMINA DEL PERSONAL :::...{funciones.RESET}\n")
    nombre = input("Ingresa el nombre a buscar: ").upper().strip()
    
    registros = crud_N.buscar(nombre, conexionBDN)
    if len(registros) > 0:
        print(f"{funciones.VERDE}\n✅ |Empleado encontrado|{funciones.RESET}")
        for fila in registros:
            print(f"🔹 ID: {fila[0]} \n🔹 Nombre: {fila[1]} \n🔹 sueldo: {fila[2]} \n🔹 sueldo_Final: {fila[3]}")
    else:
        print(f"{funciones.AMARILLO}\n⚠️ ... El empleado con ese nombre no existe ...{funciones.RESET}")
    funciones.espereTecla()

def limpiarNomina(conexionBDN):
    print(f"{funciones.CYAN}\n\t...::: 🧹 VACIAR NOMINA DEL PERSONAL  :::...{funciones.RESET}\n")
    seguro = input(f"{funciones.ROJO}¿Estas seguro de Vaciar TODO el personal? (si/No): {funciones.RESET}").lower().strip()
    
    if seguro == "si":
        respuesta = crud_N.vaciar(conexionBDN)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    else:
        print(f"{funciones.AMARILLO}\n... Operacion cancelada ...{funciones.RESET}")
        
    funciones.espereTecla()