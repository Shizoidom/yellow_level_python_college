class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]  # Стек для хранения итераторов

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                current = next(self.stack[-1])  # Берем следующий элемент из текущего итератора
                if isinstance(current, list):  # Если элемент — список, добавляем его итератор в стек
                    self.stack.append(iter(current))
                else:
                    return current  # Если элемент не список, возвращаем его
            except StopIteration:
                self.stack.pop()  # Удаляем итератор из стека, если он исчерпан
        raise StopIteration  # Если стек пуст, итерация завершена


# Пример использования
nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num, end=' ')
print()