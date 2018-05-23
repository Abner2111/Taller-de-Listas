class Nodo:
    def __init__(self, valor = None):
        self.next = None # puntero al nodo siguiente
        self.prev = None # puntero al nodo anterior
        self.valor = valor
    def get_valor(self):
        return self.valor
    def __str__(self):
        return str(self.valor)
    
class ListaDoble:
    def __init__(self):
        self.head = None # puntero al inicio de la lista
        self.tail = None # puntero al final de la lista
        self.largo = 0

    def appe(self, dato):
        self.largo += 1
        if self.head == None:
            self.head = Nodo(valor = dato)
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = Nodo(valor = dato)
            self.tail = tmp.next
            tmp.next.prev = tmp

    def reve(self):
        nodo = self.tail
        while nodo != None:
            print(nodo.__str__())
            nodo = nodo.prev
            
    def toList(self):
        nodo = self.head
        ListaN= []
        while nodo != None:
            add= nodo.get_valor()
            ListaN.append(add)
            nodo = nodo.next
        return ListaN

Prueba = ListaDoble()
Prueba.appe(1)
Prueba.appe(2)
Prueba.appe(3)
Prueba.appe(4)
Prueba.appe(5)
Prueba.appe(6)

Prueba.toList()

print(Prueba.toList()[2])

