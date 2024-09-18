class Empleado:
    def __init__(self, id_empleado, nombre, cargo, sucursal, salario):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.cargo = cargo
        self.sucursal = sucursal
        self.salario = salario

    def atender_cliente(self, cliente):
        print(f"{self.nombre} está atendiendo al cliente {cliente.nombre}")
