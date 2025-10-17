from models.administrador import Administrador
from models.supervisor import Supervisor
from models.operario import Operario
from models.vendedor import Vendedor
from empleados_repo import EmpleadosRepo

################ Arroyo Tejeda, Mayumi Naysha (PRINCIPAL) programacion de empleados_repo.py y app.py
## Yparraguirre Bravo, Ismael Jesús(APOYO) agrega excepciones restantes al ingresar DNI
## Leu Lloclla, Jhonatan Francesco (APOYO) revision de sintaxis y codigo de Naysha
def menu():
    repo = EmpleadosRepo()
    while True:
        try:
            print("\n MENÚ PRINCIPAL")
            print("1. Registrar empleado")
            print("2. Registrar asistencia")
            print("3. Registrar venta")
            print("4. Listar empleados")
            print("5. Calcular planilla")
            print("6. Salir")
            opcion = input("Seleccione opción: ")

            if opcion == "1":
                registrar_empleado(repo)
            elif opcion == "2":
                registrar_asistencia(repo)
            elif opcion == "3":
                registrar_venta(repo)
            elif opcion == "4":
                listar_empleados(repo)
            elif opcion == "5":
                calcular_planilla(repo)
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

        except Exception as e:
            print(f"Error general: {e}")
        finally:
            print("Regresando al menú principal..\n")
###############
def registrar_empleado(repo):
    print("\n REGISTRAR EMPLEADO")
    try:
        dni = input("DNI: ")
        while len(dni) != 8:
            print("El DNI debe tener exactamente 8 cifras.")
            dni = input("Ingrese nuevamente el DNI: ")

        # Verificar si el DNI ya está registrado
        if repo.obtener(dni) is not None:
            print("Error: Ya existe un empleado registrado con ese DNI.")
            return

        nombre = input("Nombre: ")

        #Area con el Número correspondiente
        print("\nSeleccione el Área:")
        print("1. Producción")
        print("2. Distribución")
        print("3. Ventas")
        print("4. Recursos Humanos")
        opcion_area = input("Opción: ")

        if opcion_area == "1":
            area = "Producción"
        elif opcion_area == "2":
            area = "Distribución"
        elif opcion_area == "3":
            area = "Ventas"
        elif opcion_area == "4":
            area = "Recursos Humanos"
        else:
            print("Error: Número de área inválido. Debe ser 1, 2, 3 o 4.")
            return

        sueldo_base = float(input("Sueldo base: "))

        print("\nTipo de empleado:")
        print("1. Administrador")
        print("2. Supervisor")
        print("3. Operario")
        print("4. Vendedor")
        tipo = input("Seleccione una opción: ")

        if tipo == "1":
            emp = Administrador(dni, nombre, area, sueldo_base)
        elif tipo == "2":
            emp = Supervisor(dni, nombre, area, sueldo_base)
        elif tipo == "3":
            emp = Operario(dni, nombre, area, sueldo_base)
        elif tipo == "4":
            emp = Vendedor(dni, nombre, area, sueldo_base)
        else:
            print("Tipo inválido.")
            return

        repo.agregar(emp)
        print(f"Empleado {nombre} registrado correctamente en el área de {area}.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Proceso de registro finalizado.\n")
################
def listar_empleados(repo):
    print("\n LISTA DE EMPLEADOS")
    try:
        empleados = repo.listar()
        if not empleados:
            print("No hay empleados registrados.")
            return
        for emp in empleados:
            print(f"{emp.get_dni()} | {emp.get_nombre()} | {emp.get_cargo()} | {emp.get_area()} | S/ .{emp.get_sueldo_base()}")
    except Exception as e:
        print(f"Error al listar empleados: {e}")
    finally:
        print("Fin de la lista de empleados.\n")

################
def registrar_asistencia(repo):
    print("\n REGISTRAR ASISTENCIA")
    try:
        dni = input("Ingrese el dni del empleado: ")
        emp = repo.obtener(dni)
        if emp is None:
            raise Exception("Empleado no encontrado.")
        emp.registrar_asistencia()
        print(f"Asistencia registrada para {emp.get_nombre()}. Total: {emp.get_asistencias()}")
    except Exception as e:
        print(f"ERROR{e}")
    finally:
        print("Fin del registro de asistencia.\n")
################
def registrar_venta(repo):
    print("\n REGISTRAR VENTA")
    try:
        dni = input("Ingrese el dni del vendedor: ")
        emp = repo.obtener(dni)
        if emp is None:
            raise Exception("Empleado no encontrado.")
        if emp.get_cargo() != "Vendedor":
            raise Exception("El empleado no es un vendedor.")
        monto = float(input("Monto de la venta: "))
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que 0.")
        emp.registrar_venta(monto)
        print(f"Venta registrada correctamente. Comisión total: {emp.get_comision()}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"ERROR {e}")
    finally:
        print("Fin del registro de venta.\n")


################
def calcular_planilla(repo):
    print("\n PLANILLAS DE PAGO")
    try:
        empleados = repo.listar()
        if not empleados:
            print("No hay empleados para calcular planilla.")
            return
        for emp in empleados:
            print(f"{emp.get_nombre()} ({emp.get_cargo()}): S/. {emp.calcular_pago()}")
    except Exception as e:
        print(f"Error al calcular planilla: {e}")
    finally:
        print("Fin del cálculo de planilla.\n")

################
if __name__ == "__main__":
    menu()
