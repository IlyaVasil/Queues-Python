from number_3.MyQueue import InterfaceQueue


class FixedQueue(InterfaceQueue):  # Фиксированная очередь
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items += [item]

    def delete(self):
        if not self.is_empty():
            self.items = self.items[0]
        else:
            print("=== Очередь пуста ===")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            print("=== Очередь пуста ===")

