from number_3.MyQueue import InterfaceQueue


class DynamicQueue(InterfaceQueue):
    def __init__(self, begin_capacity):
        self.capacity = begin_capacity
        self.items = ["·"] * begin_capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def capacity(self):
        return self.capacity

    def add(self, item):
        if self.size == self.capacity:
            self.resize()
        self.items[self.tail] = item  # Добавляем элемент в конец очереди
        self.tail = (self.tail + 1) % self.capacity  # Сдвигаем указатель конца
        self.size += 1

    def resize(self, factor=2):
        new_capacity = self.capacity * factor  # Рассчитываем новую вместимость
        new_items = ["·"] * new_capacity  # Создаем новый список большего размера

        # Копируем существующие элементы в новый список
        for i in range(self.size):
            new_items[i] = self.items[(self.head + i) % self.capacity]

        self.items = new_items  # Заменяем старый список новым
        self.head = 0  # Сбрасываем указатель начала
        self.tail = self.size  # Устанавливаем указатель конца
        self.capacity = new_capacity  # Обновляем вместимость

    def delete(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")

        item = self.items[self.head]  # Получаем элемент из начала очереди
        self.items[self.head] = '.'  # Очищаем ячейку (для сборки мусора)
        self.head = (self.head + 1) % self.capacity  # Сдвигаем указатель начала
        self.size -= 1  # Уменьшаем размер очереди
        return item  # Возвращаем удаленный элемент

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[self.head]

    def clear(self):
        self.items = ['.'] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0

