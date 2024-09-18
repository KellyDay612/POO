from inventario import Inventario

class Farmacia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sucursales = []
        self.inventario = Inventario()
        self.proveedores = []
        self.empleados = []
        self.clientes = []

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)

    def agregar_medicamento_inventario(self, proveedor, medicamento, cantidad):
        proveedor.suministrar(self.inventario, medicamento, cantidad)

    def mostrar_inventario(self):
        self.inventario.mostrar_inventario()
