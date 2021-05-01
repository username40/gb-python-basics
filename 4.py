from sys import argv
from functools import reduce
from itertools import count
from itertools import cycle

# 1.
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# пришлось закоментить решение иначе скрипт выбивает ошибку при запуске и дальше не идет по другим задачам
# script_name, hours, cost_per_hour, bonus = argv
# print((int(hours) * int(cost_per_hour)) + int(bonus))


# 3.
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])

# 4.
# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

original = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in original if original.count(i) < 2])

# 5.
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

big_list = [i for i in range(99, 1001) if i % 2 == 0]


def reducer(prev, current):
    return prev * current


print(reduce(reducer, big_list))


# 6.
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# взял пример из методички и модифицировал
def counter(start, finish):
    for el in count(start):
        if el > finish:
            break
        else:
            print(el)


counter(7, 25)


def repeater(list, finish):
    counter = 0
    for el in cycle(list):
        counter += 1
        if counter > finish:
            break
        print(el)


repeater(["python", "java", "perl", "javascript"], 10)