def get_multiplied_digits(number):
#Преобразуем число в строку
    str_number = str(number)

#Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
#Получаем первую цифру
        first = int(str_number[0])
#Умножаем первую цифру на результат рекурсивного вызова без первой цифры
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
#Если длина строки равна 1, возвращаем последнюю цифру
        return int(str_number)


#Пример использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24
