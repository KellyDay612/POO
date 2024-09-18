from cliente import Cliente
from empleado import Empleado
from proveedor import Proveedor
from medicamento import Medicamento
from categoria import Categoria
from sucursal import Sucursal
from venta import Venta
from farmacia import Farmacia

if __name__ == "__main__":
    # Crear objetos
    cliente1 = Cliente(1, "Juan Pérez", "Calle 123", "123456789", "juan@example.com")
    empleado1 = Empleado(1, "Ana López", "Cajero", "Sucursal 1", 1500)
    categoria1 = Categoria(1, "Antibiótico")
    medicamento1 = Medicamento(1, "Amoxicilina", categoria1, 10.5, 50)
    proveedor1 = Proveedor(1, "Proveedor ABC", "987654321", "abc@proveedor.com")
    sucursal1 = Sucursal(1, "Calle 456", "654321987")
    
    # Crear farmacia
    farmacia = Farmacia("Farmacia Salud")
    
    # Agregar datos
    farmacia.agregar_sucursal(sucursal1)
    farmacia.agregar_empleado(empleado1)
    farmacia.agregar_cliente(cliente1)
    farmacia.agregar_proveedor(proveedor1)
    
    # Mostrar inventario inicial
    farmacia.mostrar_inventario()
    
    # El proveedor suministra un medicamento al inventario
    farmacia.agregar_medicamento_inventario(proveedor1, medicamento1, 20)
    
    # Mostrar inventario actualizado
    farmacia.mostrar_inventario()
    
    # Realizar una venta
    venta1 = Venta(1, cliente1, empleado1, [medicamento1], 10.5)
    venta1.realizar_venta()
