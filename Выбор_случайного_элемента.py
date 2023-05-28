# Выбор случайного элемента из списка choice()
# Вы играли в детстве в «считалочки»? Эники-беники… Вот этим и занимается random.choice(): функция возвращает один случайный элемент последовательности.

# Вывод:
# ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

import random

print(list('abracadabra'))
print(random.choice(list('abracadabra')))