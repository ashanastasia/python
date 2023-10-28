class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращаем элемент из начала очереди с удалением из списка
        """
        if self.start is None:
            raise Exception("Очередь пуста")
        val = self.start.data
        if self.start is self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None
        return val

    def push(self, val):
        """
        Добавление элемента в конец очереди
        """
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        """
        Вставка элемента между элементами с номерами n-1 и n (нумерация с 0).
        """
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        elif n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            current = self.start
            for _ in range(n - 1):
                if current is None:
                    raise IndexError("Недостаточно элементов для вставки")
                current = current.nref
            if current is None:
                self.push(val)
            else:
                new_node.nref = current.nref
                new_node.pref = current
                if current.nref is not None:
                    current.nref.pref = new_node
                current.nref = new_node

    def print(self):
        """
        Вывод содержимого очереди
        """
        current = self.start
        while current is not None:
            print(current.data)
            current = current.nref

queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

queue.print()  #  1 2 3
print('/')
top_element = queue.pop()
print(top_element)  #  1
print('/')
queue.print()  #  2 3
print('/')
queue.insert(1, 4)

queue.print()  #  2 4 3
