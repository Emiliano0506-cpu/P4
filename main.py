import funciones
from personal import empleados
from nominas_de_empleados import nomina
opc = ""
conexionBD = funciones.conectar()
conexionBDN = funciones.conectar_n()

if conexionBD is not None or conexionBDN is not None:
    while opc != "3":
        funciones.borrarPantalla()
        print(f"{funciones.CYAN}\n\t\t...::: 🏢 M E N U   P R I N C I P A L :::...{funciones.RESET}\n")
        print("\t1.- 👨‍💼 Personal")
        print("\t2.- 💰 Nomina")
        print("\t3.- 🚪 Salir\n")
        opc = input("\t👉 Escribe una opcion: ").strip()

        match opc:
            case "1":
                opcion_personal = ""
                while opcion_personal != "7":
                    funciones.borrarPantalla()
                    opcion_personal = empleados.menuSecundario()

                    match opcion_personal:
                        case "1":
                            funciones.borrarPantalla()
                            empleados.agregarPersonal(conexionBD)
                        case "2":
                            funciones.borrarPantalla()
                            empleados.borrarPersonal(conexionBD)
                        case "3":
                            funciones.borrarPantalla()
                            empleados.modificarPersonal(conexionBD)
                        case "4":
                            funciones.borrarPantalla()
                            empleados.mostrarPersonal(conexionBD)
                        case "5":
                            funciones.borrarPantalla()
                            empleados.buscarPersonal(conexionBD)
                        case "6":
                            funciones.borrarPantalla()
                            empleados.limpiarPersonal(conexionBD)
                        case "7":
                            pass
                        case _:
                            funciones.borrarPantalla()
                            funciones.opcionInvalida()
                            funciones.esperarTecla()
            
            case "2":
                pass # Menu de la nomina 
                opcion_nomina = ""
                while opcion_nomina != "7":
                    funciones.borrarPantalla()
                    opcion_nomina = nomina.menuNomina()
                    match opcion_nomina:
                        case "1":
                            funciones.borrarPantalla()
                            nomina.agregarNomina(conexionBD)
                        case "2":
                            funciones.borrarPantalla()
                            nomina.borrarNomina(conexionBD)
                        case "3":
                            funciones.borrarPantalla()
                            nomina.modificarNomina(conexionBD)
                        case "4":
                            funciones.borrarPantalla()
                            nomina.mostrarNomina(conexionBD)
                        case "5":
                            funciones.borrarPantalla()
                            nomina.buscarNomina(conexionBD)
                        case "6":
                            funciones.borrarPantalla()
                            nomina.limpiarNomina(conexionBD)
                        case "7":
                            pass
            case "3":
              funciones.borrarPantalla()
              print(f"{funciones.CYAN}\n\n=============================================")
              print("  🏢 CALCULO DE NOMINAS Y PERSONAL ADMINISTRATIVO 🏢")
              print(f"============================================={funciones.RESET}")
              print("\n  🔒 Cerrando sesión de forma segura...")
              print("  ✅ Operación finalizada con éxito.")
              print(f"\n{funciones.CYAN}  ✨ ¡Que tengas un excelente día! ✨{funciones.RESET}\n")
              print(f"{funciones.CYAN}=============================================\n{funciones.RESET}")
            
              funciones.espereTecla() 
else:
    print(f"{funciones.ROJO}El sistema no puede iniciar sin base de datos.{funciones.RESET}")