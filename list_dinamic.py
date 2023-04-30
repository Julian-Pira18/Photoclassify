class dinamic_arraylist():

    def __init__(self):
        self.arreglo = []
        self.contador = 0

    def pushback(self, element):

        self.arreglo += [element]
        self.contador = self.contador + 1
        return self.arreglo

    def popback(self):
        if self.contador != 0:
            self.arreglo = self.arreglo[:-1]
            self.contador = self.contador - 1
        return self.arreglo

    def pushfront(self, element):

        new_list = [element]
        for value in self.arreglo:
            new_list += [value]
        self.arreglo = new_list

        return self.arreglo

    def pop_Front(self):
        self.arreglo = self.arreglo[1:]
        self.contador -= self.contador
        return self.arreglo

    def imprimir(self):
        for i in self.arreglo:
            print(i)
