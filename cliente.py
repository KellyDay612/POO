class Cliente:
    def __init__(self, id_cliente, nombre, direccion, telefono, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def hacer_compra(self, factura):
        print(f"{self.nombre} ha realizado una compra con la factura #{factura.id_factura}")
