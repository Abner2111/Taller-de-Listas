class Nodo:
    def __init__(self, valor = None):
        self.next = None # puntero al nodo siguiente
        self.prev = None # puntero al nodo anterior
        self.valor = valor
class ListaDoble:
    def __init__(self):
        self.head = None # puntero al inicio de la lista
        self.tail = None # puntero al final de la lista
        self.largo = 0

    def appe(self, dato):
        self.largo += 1
        if self.head == None:
            self.head = Nodo(valor = dato)
        
        
