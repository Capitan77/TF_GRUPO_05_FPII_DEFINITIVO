## Arroyo Tejeda, Mayumi Naysha 
class EmpleadosRepo:
    def __init__(self):
        self._empleados = []

    def agregar(self, empleado):
        self._empleados.append(empleado)

    def obtener(self, dni):
        for emp in self._empleados:
            if emp.get_dni() == dni:
                return emp
        return None

    def listar(self):
        return self._empleados
