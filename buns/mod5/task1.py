class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        Возвращает последний элемент из стека с удалением его из стека
        """
        if self.end is None:
            raise Exception("Стек пуст")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        Добавляет элемент val в конец стека
        """
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        """
        Выводит содержимое стека
        """
        current = self.end
        while current is not None:
            print(current.data)
            current = current.pref

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.print()  #  3 2 1
print('/')
top_element = stack.pop()
print(top_element)  # 3
print('/')
stack.print()  #  2 1
