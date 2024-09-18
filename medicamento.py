class Medicamento:
    def __init__(self, id_medicamento, nombre, categoria, precio, stock):
        self.id_medicamento = id_medicamento
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        print(f"El nuevo stock de {self.nombre} es {self.stock}")
