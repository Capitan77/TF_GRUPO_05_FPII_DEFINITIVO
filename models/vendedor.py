from models.base_empleado import Empleado
##Yparraguirre Bravo, Ismael Jesús (PRINCIPAL) desarrollo de la la superclase y las 4 clases hijos
##Rodriguez Mamani, Fernando Juan (APOYO) revision de sintaxis y codigo desarrollado por Ismael
class Vendedor(Empleado):
    def __init__(self, dni, nombre, area, sueldo_base):
        super().__init__(dni, nombre, area, sueldo_base)

    def get_cargo(self):
        return "Vendedor"

#siempre el sueldo del vendedor estara sujeto a las 
#comisiones que se generan por las ventas que hace
    def registrar_venta(self, monto):
        if monto > 0:
            comision = round(monto * 0.05, 2)
            self._sumar_comision(comision)

    def calcular_pago(self):
        return round(self.get_sueldo_base() + self.get_comision(), 2)