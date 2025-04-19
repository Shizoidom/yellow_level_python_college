def reverse_str(s, k):
    s = list(s)  # Преобразуем строку в список для изменения
    for i in range(0, len(s), 2 * k):
        # Меняем местами первые k символов каждые 2k символов
        s[i:i + k] = reversed(s[i:i + k])
    return ''.join(s)


# Примеры использования
print(reverse_str("abcdefg", 2))  # Output: "bacdfeg"
print(reverse_str("abcd", 2))     # Output: "bacd"