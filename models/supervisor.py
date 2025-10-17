from models.base_empleado import Empleado
##Yparraguirre Bravo, Ismael Jesús (PRINCIPAL) desarrollo de la la superclase y las 4 clases hijos
##Rodriguez Mamani, Fernando Juan (APOYO) revision de sintaxis y codigo desarrollado por Ismael
class Supervisor(Empleado):
    def __init__(self, dni, nombre, area, sueldo_base):
        super().__init__(dni, nombre, area, sueldo_base)

    def get_cargo(self):
        return "Supervisor"

    def calcular_pago(self):
        return round(self.get_sueldo_base(), 2)