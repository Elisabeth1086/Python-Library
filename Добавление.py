# Добавление
# Мы можем использовать функцию insert() для вставки элемента по указанному индексу. Элементы из указанного индекса сдвигаются вправо на одну позицию.

example_array = [[1, 2], [3, 4]]
example_array.insert(0, -1)
example_array.insert(2, [-1, 13, 64])
print(example_array)

# Вывод:
# [-1, [1, 2], [-1, 13, 64], [3, 4]]

# Если вам нужно добавить элемент в конец массива, используйте функцию append().

example_array = [[1, 2], [3, 4]]
example_array.append(-1)
example_array.append([-1, 13, 64])
print(example_array)

# Вывод:
# [[1, 2], [3, 4], -1, [-1, 13, 64]]

# Для того, чтоб объединить элементы двух массивов используйте метод extend.

example_array = [1, 2, 3, 4]
example_array.extend([5, 6])
print(example_array)

# Вывод:
# [1, 2, 3, 4, 5, 6]