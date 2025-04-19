def create_abbreviation(phrase):
    words = phrase.split()  # Разделяем фразу на слова по пробелам
    abbreviation = ""
    for word in words:
        if word[0].isalpha():  # Проверяем, начинается ли слово с буквы
            abbreviation += word[0].upper()  # Добавляем первую букву в верхнем регистре
    return abbreviation


# Примеры использования
print(create_abbreviation("Today I learned"))  # Ожидаемый результат: TIL
print(create_abbreviation("Высшее учебное заведение"))  # Ожидаемый результат: ВУЗ
print(create_abbreviation("Кот обладает талантом"))  # Ожидаемый результат: КОТ
print(create_abbreviation("Ар 2 Ди #2"))  # Ожидаемый результат: АД
print(create_abbreviation("Анна-Мария Волхонская"))  # Ожидаемый результат: АВ