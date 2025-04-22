class DynamicStack:

    def __init__(self, capacity=4):

        self.capacity = capacity  # Начальная емкость стека
        self.items = ['.'] * capacity  # Список для хранения элементов стека
        self.top = -1  # Индекс вершины стека (-1 означает пустой стек)
        self.size = 0  # Текущее количество элементов в стеке

    def is_empty(self):

        return self.top == -1

    def is_full(self):

        return self.size == self.capacity

    def add(self, item):

        if self.is_full():
            self._resize()  # Удваиваем емкость, если стек полон

        self.top += 1
        self.items[self.top] = item
        self.size += 1

    def delete(self):

        if self.is_empty():
            print("Стек пуст.")
            return None

        item = self.items[self.top]
        self.items[self.top] = '.'  # Освобождаем ячейку, чтобы не хранить ссылку на объект
        self.top -= 1
        self.size -= 1

        return item

    def peek(self):

        if self.is_empty():
            print("Стек пуст.")

        return self.items[self.top]

    def _resize(self):

        new_capacity = self.capacity * 2
        new_stack = ['.'] * new_capacity
        for i in range(self.capacity):
            new_stack[i] = self.items[i]
        self.items = new_stack
        self.capacity = new_capacity
        print(f"Емкость стека увеличена до: {self.capacity}")
