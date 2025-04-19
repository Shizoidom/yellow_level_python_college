def count_digits(number):
    digit_count = {str(digit): 0 for digit in range(10)}  # Инициализируем словарь для подсчета цифр
    for digit in str(number):  # Преобразуем число в строку и перебираем символы
        digit_count[digit] += 1  # Увеличиваем счетчик для соответствующей цифры
    return digit_count


# Пример использования
number = int(input("Введите положительное целое число: "))
result = count_digits(number)
print("Частота цифр в числе:")
for digit, count in result.items():
    print(f"{digit}: {count}")