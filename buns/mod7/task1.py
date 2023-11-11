class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def get(self, index):
        if not self.head:
            raise IndexError("Список пуст")
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Индекс вне диапазона")
    def remove(self, index):
        if not self.head:
            raise IndexError("Список пуст")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                current.next = current.next.next
                return
            current = current.next
            count += 1
        raise IndexError("Индекс вне диапазона")
    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current:
                if count == n - 1:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
                count += 1
            raise IndexError("Индекс вне диапазона")
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
# Пример использования
my_list = LinkedList()
my_list.push(1)
my_list.push(2)
my_list.push(3)
print("Список:")
for item in my_list:
    print(item)
print("Элемент с индексом 1:", my_list.get(1))
my_list.remove(0)
print("Список после удаления элемента с индексом 0:")
for item in my_list:
    print(item)
my_list.insert(1, 4)
print("Список после вставки элемента 4 на позицию 1:")
for item in my_list:
    print(item)
