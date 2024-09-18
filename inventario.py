class Inventario:
    def __init__(self):
        self.medicamentos = {}

    def agregar_medicamento(self, medicamento, cantidad):
        if medicamento.id_medicamento in self.medicamentos:
            self.medicamentos[medicamento.id_medicamento].actualizar_stock(cantidad)
        else:
            medicamento.actualizar_stock(cantidad)
            self.medicamentos[medicamento.id_medicamento] = medicamento

    def mostrar_inventario(self):
        for medicamento in self.medicamentos.values():
            print(f"{medicamento.nombre}: {medicamento.stock} unidades disponibles")
