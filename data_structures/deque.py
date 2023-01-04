"""
Deque() создаёт новый пустой дек. Не нуждается в параметрах и возвращает
    пустой дек.
addFront(item) добавляет новый элемент в голову дека. Параметр (элемент)
    необходим; ничего не возвращает.
addRear(item) добавляет новый элемент в хвост дека. Параметр (элемент) необходим;
    ничего не возвращает.
removeFront() удаляет первый элемент из дека. Не нуждается в параметрах и
    возвращает элемент. Дек модифицируется.
removeRear() удаляет последний элемент из дека. Не нуждается в параметрах и
    возвращает элемент. Дек модифицируется.
isEmpty() проверяет дек на пустоту. Не нуждается в параметрах и возвращает
    булево значение.
size() возвращает количество элементов в деке. Не нуждается в параметрах и
    возвращает целое число.
"""


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    d = Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
