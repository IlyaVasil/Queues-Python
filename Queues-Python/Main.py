import random

from Fixed_Queue import FixedQueue
from Fixed_Stack import FixedStack
from DynamicQueue import DynamicQueue
from DynamicStack import DynamicStack
from Ring_Queue import RingQueue
from Ring_Stack import RingStack
from RingDynamicQueue import RingDynamicQueue

while True:

    number = int(input(
        " === 1. Фиксированная очередь === \n "
        " === 2. Фиксированный стек === \n "
        " === 3. Кольцельвая очередь === \n "
        " === 4. Кольцевой стек === \n "
        " === 5. Динамическая очередь === \n "
        " === 6. Динамический стек === \n "
        " === 7. Кольцевая-динамическая очередь === \n "
        " === 8. Кольцевой-динамический стек === \n "
        " === 9. Выход === \n "
        " Выберите пункт,который хотите выбрать: \n"))

    """ФИКСИРОВАННАЯ ОЧЕРЕДЬ"""

    if number == 1:
        print(" === Вы выбрали фиксированную очередь === ")
        queue = FixedQueue()
        n = int(input("Введите размер очереди:"))
        while True:
            queue_number = int(
                input(
                    " 1. Добавление \n"
                    " 2. Удаление \n"
                    " 3. Выход \n "
                    " Выберите пункт,который хотите выбрать: "))
            if queue_number == 1:
                queue_add = int(input(
                    " === Выберите способ заполнения: === \n "
                    " 1. Вручную \n"
                    " 2. Автоматически \n"
                    " === Вы выбрали добавление в очередь ===  \n"))
                if queue_add == 1:
                    for i in range(0, n):
                        T = int(input("Введите значение"))
                        queue.add(T)
                    print("Элементы очереди " + str(queue.items))
                elif queue_add == 2:
                    for i in range(0, n):
                        T = random.randint(1, 100)
                        try:
                            queue.add(T)
                        except IndexError as e:
                            print("Ошибка при добавлении элемента")
                            break
                    print("Элементы очереди " + str(queue.items))

            elif queue_number == 2:
                print("=== Вы выбрали удаление элементов === ")
                queue.delete()
                print("Вывод всех элементов " + str(queue.items))
                print("Последний элемент: " + str(queue.peek()))
            elif queue_number == 3:
                print("Выход из программы")
                break

            """ФИКСИРОВАННАЯ ОЧЕРЕДЬ"""

            """ФИКСИРОВАННЫЙ СТЕК"""
    elif number == 2:
        print(" === Вы выбрали фиксированный стек === ")
        stack = FixedStack()
        while True:
            stack_number = int(
                input(
                    " 1.Добавление \n"
                    " 2.Удаление \n "
                    " 3.Выход \n "
                    " ===Выберите пункт,который хотите выбрать:=== \n"))
            if stack_number == 1:
                print("Вы выбрали добавление в стек")
                n = int(input("Введите размер очереди"))
                add_fix_stack = int(input(
                    "===Добавление в фиксированный стек=== \n "
                    " 1. Вручную \n"
                    " 2. Автоматически \n"
                    " 3. Выход \n"
                    " ===Выберите пункт,который хотите выбрать:==="))
                if add_fix_stack == 1:
                    for i in range(0, n):
                        T = int(input("Введите значение"))
                        stack.add(T)
                    print("Элементы cтека " + str(stack.items))
                elif add_fix_stack == 2:
                    for i in range(0, n):
                        T = random.randint(1, 100)
                        try:
                            stack.add(T)
                        except IndexError as e:
                            print("Ошибка при добавлении элемента")
                            break
                    print("Элементы очереди " + str(stack.items))

            elif stack_number == 2:
                print("Вы выбрали удаление из стека")
                print("Удаленный элемент " + str(stack.peek()))
                stack.delete()
                print("Последний элемент " + str(stack.peek()))
                print("Вывод всех элементов " + str(stack.items))
            elif stack_number == 3:
                print("Выход из программы")
                break

            """ФИКСИРОВАННЫЙ СТЕК"""

            """КОЛЬЦЕВАЯ ОЧЕРЕДЬ"""

    elif number == 3:
        print("Вы выбрали кольцевую очередь")
        capacity = int(input("Введите размер очереди"))
        ring_queue = RingQueue(capacity)
        while True:
            ring_queue_number = int(
                input(
                    "\n 1. Добавление"
                    "\n 2. Удаление"
                    "\n 3. Выход"
                    "\n === Выберите пункт,который хотите выбрать: === ")
            )
            if ring_queue_number == 1:

                print("Вы выбрали добавление в очередь")

                T = int(input("Введите значение: \n"))
                ring_queue.add(T)
                print("Элементы очереди " + str(ring_queue.items))

            elif ring_queue_number == 2:
                print("Вы выбрали удаление элементов ")
                ring_queue.delete()
                print("Вывод всех элементов " + str(ring_queue.items))
                print("Последний элемент " + str(ring_queue.peek()))

            elif ring_queue_number == 3:
                print("Выход из программы")
                break

            """КОЛЬЦЕВАЯ ОЧЕРЕДЬ"""

            """КОЛЬЦЕВОЙ СТЕК"""
    elif number == 4:
        print("Вы выбрали кольцевой стек")
        capacity = int(input("Введите размер стека"))
        ring_stack = RingStack(capacity)
        while True:
            ring_queue_number = int(
                input("Выберите пункт,который хотите выбрать: \n "
                      "1.Добавление \n "
                      "2.Удаление\n "
                      "3.Выход\n"))
            if ring_queue_number == 1:

                print("Вы выбрали добавление в стек")
                try:
                    T = int(input("Введите значение \n"))
                    ring_stack.add(T)  # Добавление элемента
                    print("Элементы стека " + str(ring_stack.items))
                    print("Последний эелемент стека " + str(ring_stack.peek()))
                except ValueError:
                    print("Некорректный ввод, введите число")
            elif ring_queue_number == 2:
                print("Вы выбрали удаление элементов ")
                ring_stack.delete()  # Удаление элемента
                print("Вывод всех элементов " + str(ring_stack.items))
                print("Последний элемент " + str(ring_stack.peek()))

            elif ring_queue_number == 3:
                print("Выход из программы")
                break

            """КОЛЬЦЕВОЙ СТЕК"""

            """ДИНАМИЧЕСКАЯ ОЧЕРЕДЬ"""

    elif number == 5:
        n = int(input("Введите размер очереди:"))
        dinamic_queue = DynamicQueue(n)
        while True:
            din_queue = int(
                input("=== Вы выбрали динамическую очередь === "
                      "\n 1. Добавление \n 2. Удаление \n 3. Выход \n"))
            if din_queue == 1:
                din_queue_choise = int(input(
                    "=== Вы выбрали добавление, как вы хотите заполнить очередь? === \n "
                    " 1. Автоматически  \n  2. Вручную \n"))
                if din_queue_choise == 1:
                    for i in range(0, n):
                        T = random.randint(1, 100)
                        dinamic_queue.add(T)
                    print("Элементы очереди " + str(dinamic_queue.items))
                elif din_queue_choise == 2:
                    try:
                        T = int(input("Введите значение"))
                        dinamic_queue.add(T)
                    except IndexError as e:
                        print("Ошибка при добавлении элемента")
                    print("Элементы очереди " + str(dinamic_queue.items))

            elif din_queue == 2:
                print("=== Вы выбрали удаление элементов === ")
                dinamic_queue.delete()
                print("Вывод всех элементов " + str(dinamic_queue.items))
                try:
                    print("Последний элемент " + str(dinamic_queue.peek()))
                except IndexError:
                    print("Очередь пуста")
            elif din_queue == 3:
                break

        """ДИНАМИЧЕСКАЯ ОЧЕРЕДЬ"""

        """ДИНАМИЧЕСКИЙ СТЕК"""
    elif number == 6:
        print("Вы выбрали динамический стек:")
        n = int(input("Введите размер стека \n"))
        dinamic_stack = DynamicStack(n)

        while True:
            dyn_stack = int(
                input("=== Вы выбрали динамический стек === "
                      "\n 1. Добавление \n 2. Удаление \n 3. Выход \n"))
            if dyn_stack == 1:
                dyn_stack_choise = int(input(
                    "=== Вы выбрали добавление, как вы хотите заполнить стек? === \n "
                    " 1. Автоматически  \n  2. Вручную \n"))
                if dyn_stack_choise == 1:
                    for i in range(0, n):
                        T = random.randint(1, 100)
                        dinamic_stack.add(T)
                    print("Элементы стека " + str(dinamic_stack.items))
                elif dyn_stack_choise == 2:
                    try:
                        T = int(input("Введите значение"))
                        dinamic_stack.add(T)
                    except IndexError as e:
                        print("Ошибка при добавлении элемента")
                    print("Элементы стека " + str(dinamic_stack.items))

            elif dyn_stack == 2:
                print("=== Вы выбрали удаление элементов === ")
                dinamic_stack.delete()
                print("Вывод всех элементов " + str(dinamic_stack.items))
                try:
                    print("Последний элемент " + str(dinamic_stack.peek()))
                except IndexError:
                    print("Стек пуст!")
            elif dyn_stack == 3:
                break

        """ДИНАМИЧЕСКИЙ СТЕК"""

        """КОЛЬЦЕВАЯ ДИНАМИЧЕСКАЯ ОЧЕРЕДЬ"""
    elif number == 7:
        print("Вы выбрали кольцевую-динамическую очередь:")
        n = int(input("Введите размер очереди \n"))
        ring_dynamic_queue = RingDynamicQueue(n)

        while True:
            dyn_stack = int(
                input("=== Вы выбрали кольцевую-динамическую очередь === "
                      "\n 1. Добавление \n 2. Удаление \n 3. Выход \n"))
            if dyn_stack == 1:
                dyn_stack_choise = int(input(
                    "=== Вы выбрали добавление, как вы хотите заполнить стек? === \n "
                    " 1. Автоматически  \n  2. Вручную \n"))
                if dyn_stack_choise == 1:
                    for i in range(0, n):
                        T = random.randint(1, 100)
                        ring_dynamic_queue.add(T)
                    print("Элементы очереди " + str(ring_dynamic_queue.items))
                elif dyn_stack_choise == 2:
                    try:
                        T = int(input("Введите значение"))
                        ring_dynamic_queue.add(T)
                    except IndexError as e:
                        print("Ошибка при добавлении элемента")
                    print("Элементы очереди " + str(ring_dynamic_queue.items))

            elif dyn_stack == 2:
                print("=== Вы выбрали удаление элементов === ")
                ring_dynamic_queue.delete()
                print("Вывод всех элементов " + str(ring_dynamic_queue.items))
                try:
                    print("Последний элемент " + str(ring_dynamic_queue.peek()))
                except IndexError:
                    print("очередь пуста!")
            elif dyn_stack == 3:
                break
        """КОЛЬЦЕВАЯ ДИНАМИЧЕСКАЯ ОЧЕРЕДЬ"""

        """КОЛЬЦЕВОЙ ДИНАМИЧЕСКИЙ СТЕК"""
    elif number == 8:
        print("Вы выбрали кольцевую-динамическую очередь:")
        n = int(input("Введите размер стека \n"))
        dinamic_stack = DynamicStack(n)

        while True:
            dyn_stack = int(
                input("=== Вы выбрали кольцевую-динамическую очередь === "
                      "\n 1. Добавление \n 2. Удаление \n 3. Выход \n"))
            if dyn_stack == 1:
                dyn_stack_choise = int(input(
                    "=== Вы выбрали добавление, как вы хотите заполнить стек? === \n "
                    " 1. Автоматически  \n  2. Вручную \n"))
                if dyn_stack_choise == 1:
                    for i in range(0, n):
                        T = random.randint(1, 100)
                        dinamic_stack.add(T)
                    print("Элементы очереди " + str(dinamic_stack.items))
                elif dyn_stack_choise == 2:
                    try:
                        T = int(input("Введите значение"))
                        dinamic_stack.add(T)
                    except IndexError as e:
                        print("Ошибка при добавлении элемента")
                    print("Элементы очереди " + str(dinamic_stack.items))

            elif dyn_stack == 2:
                print("=== Вы выбрали удаление элементов === ")
                dinamic_stack.delete()
                print("Вывод всех элементов " + str(dinamic_stack.items))
                try:
                    print("Последний элемент " + str(dinamic_stack.peek()))
                except IndexError:
                    print("очередь пуста!")
            elif dyn_stack == 3:
                break
        """КОЛЬЦЕВОЙ ДИНАМИЧЕСКИЙ СТЕК"""

    elif number == 9:
        print("Выход из программы")
    break
