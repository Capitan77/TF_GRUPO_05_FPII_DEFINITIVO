from models.base_empleado import Empleado
##Yparraguirre Bravo, Ismael Jesús (PRINCIPAL)
##Rodriguez Mamani, Fernando Juan (APOYO)
class Administrador(Empleado):
    def __init__(self, dni, nombre, area, sueldo_base):
        super().__init__(dni, nombre, area, sueldo_base)

    def get_cargo(self):
        return "Administrador"

    def calcular_pago(self):
        return round(self.get_sueldo_base(), 2)