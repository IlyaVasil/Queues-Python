class RingDynamicQueue:


    def __init__(self, capacity=4):

        self.capacity = capacity
        self.items = ['.'] * capacity
        self.head = 0  # Индекс начала очереди
        self.tail = 0  # Индекс конца очереди
        self.size = 0  # Текущий размер очереди

    def is_empty(self):

        return self.size == 0

    def is_full(self):

        return self.size == self.capacity

    def add(self, item):

        if self.is_full():
            self._resize()

        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def delete(self):

        if self.is_empty():
            return 'Очередь пуста!'

        item = self.items[self.head]
        self.items[self.head] = '.'  # Освобождаем ячейку, чтобы не хранить ссылку
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """
        Возвращает элемент из начала очереди, не удаляя его.

        Returns:
            Элемент из начала очереди, или None, если очередь пуста.
        """
        if self.is_empty():
            return None
        return self.items[self.head]

    def _resize(self):

        new_capacity = self.capacity * 2
        new_queue = ['.'] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.items[(self.head + i) % self.capacity]
        self.items = new_queue
        self.head = 0
        self.tail = self.size
        self.capacity = new_capacity
