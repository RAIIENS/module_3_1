# Создаём глобальную переменную `calls`, которая изначально будет равна 0.
# Она будет подсчитывать колличество вызовов функций.
calls = 0
#  Создадим функцию `count_calls`, она будет увеличивать значение переменной `calls` на 1
#  каждый раз, когда она будет вызываться.
def count_calls():
    global calls  # Указываем, что используем глобальную переменную
    calls += 1  # Увеличиваем счетчик вызовов на 1

def string_info(string):
# Эту функцию будем использовать для обработки строки
    count_calls()  # Увеличиваем счетчик вызовов

    length = len(string)  # Длина строки
    upper_case = string.upper()  # Строка в верхнем регистре
    lower_case = string.lower()  # Строка в нижнем регистре
    return (length, upper_case, lower_case)  # Возвращаем кортеж

# проверяем вхождение строки в список
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов

# Приводим строку и элементы списка к нижнему регистру для сравнения
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)
# Возвращаем результат проверки
# Вызываем функции с произвольными данными
result1 = string_info("Москва")
result2 = is_contains("Плюс", ["Ева", "Москва", "Диана"])
# Выводим результаты
print("Результат функции string_info:", result1)
print("Результат функции is_contains:", result2)
# Выводим количество вызовов функций
print("Количество вызовов функций:", calls)


#  Итог выполненной работы:
#
# 1. Создали глобальную переменную `calls`, которая будет хранить количество вызовов.
# 2. Создали функцию `count_calls` которая изменяет значение `calls`, увеличивая его на 1.
# 3. Создали функцию `string_info` которая вычисляет длину строки и возвращаем её в
#    двух регистрах. Причем Каждый вызов этой функции увеличивает счётчик вызовов.
# 4. Функция `is_contains` проверяет, находится ли наша строка в списке (игнорируя регистр).
#    Она также увеличивает счётчик вызовов.
# 5. В конце мы выводим результаты работы функций и общее количество вызовов.
