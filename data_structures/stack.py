"""
Stack() создаёт новый пустой стек. Параметры не нужны, возвращает пустой стек.
push(item) добавляет новый элемент на вершину стека.
    В качестве параметра выступает элемент; функция ничего не возвращает.
pop() удаляет верхний элемент из стека. Параметры не требуются,
    функция возвращает элемент. Стек изменяется.
peek() возвращает верхний элемент стека, но не удаляет его.
    Параметры не требуются, стек не модифицируется.
isEmpty() проверяет стек на пустоту. Параметры не требуются,
    возвращает булево значение.
size() возвращает количество элементов в стеке. Параметры не требуются,
    тип результата - целое число.
"""


class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()

    print(s.isempty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isempty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
