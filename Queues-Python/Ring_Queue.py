from number_3.MyQueue import InterfaceQueue


class RingQueue(InterfaceQueue):  # Кольцевая очередь

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def full_ring_queue(self):  # Проверка на заполненность очереди
        return self.size == self.capacity

    def add(self, item):
        if self.full_ring_queue():
            self.delete()
            self.items[self.tail] = item
            self.head = (self.head + 1) % self.capacity
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1

    def is_empty(self):
        return self.size == 0

    def delete(self):
        item = self.items[self.head]
        self.items[self.head] = "·"
        self.head = (self.head + 1) % self.capacity
        return print(f"Удаленный элемент: {item}")

    def peek(self):
        return self.items[self.head]

