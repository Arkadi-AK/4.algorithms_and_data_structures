"""
Queue() создаёт новую пустую очередь. Не нуждается в параметрах,
    возвращает пустую очередь.
enqueue(item) добавляет новый элемент в конец очереди.
    Требует элемент в качестве параметра, ничего не возвращает.
dequeue() удаляет из очереди передний элемент. Не нуждается в параметрах,
    возвращает элемент. Очередь изменяется.
isEmpty() проверяет очередь на пустоту. Не нуждается в параметрах,
    возвращает булево значение.
size() возвращает количество элементов в очереди (целое число).
    Не нуждается в параметрах.
"""


class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q.isempty())
    q.enqueue('dog')
    q.enqueue(4)
    print(q.isempty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
