# В Python удалить ненужные элементы из массива можно при помощи метода pop, аргументом которого является индекс ячейки. 
# Как и в случае с добавлением нового элемента, метод необходимо вызвать через ранее созданный объект.

example_array = [1, 2, 6, 3, 4]
print(example_array.pop(4))
print(example_array)

# Вывод:
# 4
# [1, 2, 6, 3]

# После выполнения данной операции содержимое массива сдвигается так, чтобы количество доступных ячеек памяти совпадало с текущим количеством элементов.