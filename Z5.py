def get_row(rowIndex):
    row = [1]  # Начинаем с первой строки
    for _ in range(rowIndex):
        # Формируем следующую строку на основе текущей
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row


# Примеры использования
print(get_row(3))  # Output: [1, 3, 3, 1]
print(get_row(0))  # Output: [1]
print(get_row(1))  # Output: [1, 1]
print(get_row(2))  # Output: [1, 2, 1]
print(get_row(4))  # Output: [1, 4, 6, 4, 1]
print(get_row(5))  # Output: [1, 5, 10, 10, 5, 1]
print(get_row(6))  # Output: [1, 6, 15, 20, 15, 6, 1]