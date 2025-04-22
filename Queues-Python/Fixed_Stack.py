from number_3.MyQueue import InterfaceQueue


class FixedStack(InterfaceQueue):  # Фиксированный стек

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, item):  # Добавление элементов в стек
        self.items += [item]

    def delete(self):  # Удаление и возврат элемента с вершины стека
        if self.is_empty():
            print(self.items)
            raise IndexError("Стек пуст!")
        else:
            self.items = self.items[:-1]

    def peek(self):  # Возврат элемента без удаления
        if self.is_empty():
            print(self.items)
            raise IndexError("Стек пуст!")
        return self.items[-1]
