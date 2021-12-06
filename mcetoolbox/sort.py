class Sort:
    def bubbleSort(self, lista):
        aux = lista.head
        while aux is not None:
            aux2 = aux.getNext()
            while aux2 is not None:
                if aux.getData() > aux2.getData():
                    temp = aux.getData()
                    aux.setData(aux2.getData())
                    aux2.setData(temp)
                aux2 = aux2.getNext()
            aux = aux.getNext()
        return lista

    def shellSort(self, lista):
        gap = lista.len // 2
        while gap > 0:
            for i in range(gap, lista.len):
                temp = lista.getIndex(i).getData()
                j = i
                while j >= gap and lista.getIndex(j - gap).getData() > temp:
                    lista.getIndex(j).setData(
                        lista.getIndex(j - gap).getData())
                    j -= gap
                lista.getIndex(j).setData(temp)
            gap //= 2
        return lista

    def insertionSort(self, lista):
        for i in range(1, lista.len):
            for j in range(i, 0, -1):
                if lista.getIndex(j).getData() < lista.getIndex(j-1).getData():
                    lista.swap(j, j-1)
                else:
                    break
        return lista

    def selectionSort(self, lista):
        for i in range(lista.len - 1):
            min = i
            for j in range(i + 1, lista.len):
                if lista.getIndex(j).getData() < lista.getIndex(min).getData():
                    min = j
            lista.swap(i, min)   # troca os valores
        return lista
