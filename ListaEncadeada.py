class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEncadeada:
    def __init__(self):
        self.head = None
        self._size = 0

    # COMPLEXIDADE DO ALGORITIMO APPEND -> 0[N]
    def append(self, elemento):
        if self.head:
            # inserção quando a lista já possui elementos
            ponteiro = self.head
            while ponteiro.next:
                ponteiro = ponteiro.next
            ponteiro.next = Node(elemento)
        else:
            self.head = Node(elemento)  # Primeira inserção
        self._size = self._size + 1

    #    @property
    # CONSTANTE
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def _getnode(self, index):
        # a = lista.get(6)
        ponteiro = self.head
        for i in range(index):
            if ponteiro:
                ponteiro = ponteiro.next
            else:
                raise IndexError("Índex Desconhecido")
        return ponteiro

    def set(self, index, elemento):
        # lista.set(5, 9)
        pass

    # COMPLEXIDADE DO ALGORITIMO GETITEM -> 0[N]
    def __getitem__(self, index):
        # a = lista[6]
        # a = lista.get(6)

        ponteiro = self._getnode(index)
        if ponteiro:
            return ponteiro.data
        else:
            raise IndexError("Índex Desconhecido")

    # COMPLEXIDADE DO ALGORITIMO SETITEM -> 0[N]
    def __setitem__(self, index, elemento):
        # lista[5] = 9
        # lista.set(5, 9)

        ponteiro = self._getnode(index)
        if ponteiro:
            ponteiro.data = elemento
        else:
            raise IndexError("Índex Desconhecido")

    # COMPLEXIDADE DO ALGORITIMO BUSCA -> 0[N]
    def busca(self, elemento):
        """Returna o indice elem se ele estiver na lista ou none, caso contrário"""
        ponteiro = self.head
        i = 0
        while ponteiro:
            if ponteiro.data == elemento:
                return i
            ponteiro = ponteiro.next
            i = i + 1
        raise ValueError("{} - Esse elemento não está na lista".format(elemento))

    # COMPLEXIDADE DO ALGORITIMO BUSCA -> 0[N]
    def insert(self, index, elemento):  # inserção de elemento em qualquer posição
        node = Node(elemento)
        if index == 0:   # O[1]
            node.next = self.head
            self.head = node
        else:
            ponteiro = self._getnode(index - 1)
            node = Node(elemento)
            node.next = ponteiro.next
            ponteiro.next = node
        self._size = self._size + 1

    # COMPLEXIDADE DO ALGORITIMO BUSCA -> 0[N]
    def remove(self, elemento):
        if self.head is None:
            raise ValueError("{} - Esse elemento não está na lista".format(elemento))
        elif self.head.next == elemento:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            antecessor = self.head
            ponteiro = self.head.next
            while ponteiro:
                if ponteiro.data == elemento:
                    antecessor.next = ponteiro.next
                    ponteiro.next = None
                antecessor = ponteiro
                ponteiro = ponteiro.next
            self._size = self._size - 1
            return True
#        raise ValueError("{} - Esse elemento não está na lista".format(elemento))

    def __repr__(self):
        r = ""
        ponteiro = self.head
        while ponteiro:
            r = r + str(ponteiro.data) + " -> "
            ponteiro = ponteiro.next
        return r

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    lista = ListaEncadeada()

    lista.append(23)
    lista.append(14)
    lista.append(5)
    lista.append(60)
    lista.append(10)
    lista.append(24)
''' 
    TIPOS DE FUNÇÕES DE BUSCAS

    def busca(self, elemento):
    """Returna o indice elem se ele estiver na lista ou none, caso contrário"""
    for index in range(len(self)):
        if self[index] == elemento:
            return index
        else:
            raise IndexError("list index out of range")
    return None
    
    def busca(LinkedList, elemento):
        """Returna o indice elem se ele estiver na lista ou none, caso contrário"""
        for i in range(len(LinkedList)):
            if LinkedList[i] == elemento:
                return i
        return None
'''

"""
TIPOS DE FUNÇÕES DE MOSTRAR INDEX

    ### DEU RUIM ###
    
indice = busca(LinkedList, data)
if indice is not None:
    print("O indice do elemento {} é {}".format(data, indice))
else:
    print('O elemento {} não se encontra na lista'.format(data))
"""

'''
    COMANDOS PARA EXECUTAR EM TESTES

lista = LinkedList()

lista.append(23)
lista.append(14)
lista.append(5)
lista.append(60)
lista.append(10)
lista.append(24)

lista.busca(23)

lista [0]

len(lista)

lista.insert(3, 888)

lista.insert(len(lista), 50  # para colocar no final da lista

lista[len(lista)-1]  # para ver o ultimo elemento da lista

lista.remove(80)



'''
