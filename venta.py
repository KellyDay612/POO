from factura import Factura

class Venta:
    def __init__(self, id_venta, cliente, empleado, medicamentos, total):
        self.id_venta = id_venta
        self.cliente = cliente
        self.empleado = empleado
        self.medicamentos = medicamentos
        self.total = total

    def realizar_venta(self):
        factura = Factura(self.id_venta, self.cliente, self.empleado, self.medicamentos, self.total)
        self.cliente.hacer_compra(factura)
        factura.mostrar_factura()
