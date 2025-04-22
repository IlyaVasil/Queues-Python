from number_3.MyQueue import InterfaceQueue


class RingStack(InterfaceQueue):  # Кольцевая очередь

    def __init__(self, capacity):

        self.capacity = capacity
        self.items = ["·"] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def full_ring_stack(self):  # Проверка на заполненность очереди
        return self.size == self.capacity

    def add(self, item):  # Добавление элемента
        if self.full_ring_stack():
            self.delete()

        self.items[self.tail] = item  # Добавляем элемент в текущую позицию tail
        self.tail = (self.tail + 1) % self.capacity  # Сдвигаем tail (указывает на вершину)

        if self.size < self.capacity:
            self.size += 1  # Увеличиваем размер, если стек еще не заполнен
        else:
            self.head = (self.head + 1) % self.capacity

    def is_empty(self):  # Проверка, заполнена ли очередь
        return self.size == 0

    def delete(self):  # Удаление элемента
        if self.is_empty():
            raise IndexError("Стек пуст")
        self.items[self.tail] = '·'  # Очищаем ячейку
        self.tail = (self.tail + 1 + self.capacity) % self.capacity  # Сдвигаем tail назад
        item = self.items[self.tail]  # Получаем элемент с вершины

        return item

    def peek(self):  # Извлечение последнего элемента
        if self.is_empty():
            raise IndexError("Стек пуст")
            # Вычисляем индекс вершины (последнего элемента)
        peak_index = (self.tail - 1 + self.capacity) % self.capacity
        return self.items[peak_index]


