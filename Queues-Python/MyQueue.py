from abc import ABC, abstractmethod

"""Интерфейсы"""


class InterfaceQueue(ABC):
    """Методы для фиксированной очереди"""

    @abstractmethod
    def is_empty(self):  # Пустая ли очередь
        pass

    @abstractmethod
    def add(self, item):  # Добавление в очередь
        pass

    @abstractmethod
    def delete(self):  # Удаление элемента
        pass

    @abstractmethod
    def peek(self):  # Возврат последнего элемента
        pass


