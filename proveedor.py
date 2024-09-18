class Proveedor:
    def __init__(self, id_proveedor, nombre, telefono, email):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def suministrar(self, inventario, medicamento, cantidad):
        inventario.agregar_medicamento(medicamento, cantidad)
        print(f"{self.nombre} ha suministrado {cantidad} unidades de {medicamento.nombre} al inventario.")
