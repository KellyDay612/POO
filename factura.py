class Factura:
    def __init__(self, id_factura, cliente, empleado, lista_medicamentos, total):
        self.id_factura = id_factura
        self.cliente = cliente
        self.empleado = empleado
        self.lista_medicamentos = lista_medicamentos
        self.total = total

    def mostrar_factura(self):
        print(f"Factura #{self.id_factura}:")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Atendido por: {self.empleado.nombre}")
        print(f"Medicamentos comprados: {[med.nombre for med in self.lista_medicamentos]}")
        print(f"Total: {self.total} USD")
