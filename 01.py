# 1
# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
numberVar = 11
stringVar = 'String'

whatTime = input('what time? ')

print(f"now is {whatTime} o'clock!")

# 2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
print('не осилил задание 2')

# 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = input('enter number')
# можно сделать через раскидывание по переменным
one = int(num)
two = int(num + num)
three = int(num + num + num)
print(f'{one} + {two} + {three} = {one + two + three}')

# либо конечно в одну строку, но читать такое уже не просто
print(f'{int(num)} + {int(num * 2)} + {int(num * 3)} = {int(num) + int(num * 2) + int(num * 3)}')

# 4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
print('не осилил задание 4')

# 5
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

plus = float(input('Выручка: '))
minus = float(input('Расходы: '))
if plus > minus:
    # не понял как расчитать отношение, времени спрашивать среди ночи особо не было ((
    print('Фирма работает с прибылью')
    employees = int(input('Количество сотрудников: '))
    print(f'прибыль в расчете на одного сторудника сотавила {(plus - minus) / employees}')
elif plus == minus:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

# 6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

run_now = int(input('Сколько бегаешь сейчас? '))
run_want = int(input('Сколько хочешь пробежать? '))

counter = 0

while run_now < run_want:
    run_now += run_now / 10
    counter +=1

print(f'Для того чтобы пробежать {run_want}км необходимо {counter}дн. В последний день ты пробежишь {run_now}км')



