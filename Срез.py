# Срез
# Срез Python предоставляет особый способ создания массива из другого массива.

example_array = [[1, 2], [3, 4]]
print(example_array[::-1])
print(example_array[1:])
print(example_array[0][:-1])

# Вывод:
# [[3, 4], [1, 2]]
# [[3, 4]]
# [1]