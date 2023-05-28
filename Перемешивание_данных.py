# Перемешивание данных — shuffle()
# Метод random.shuffle() применяется для расстановки элементов последовательности в случайном порядке. 

# Представьте коробку в которой лежат какие-то предметы. Встряхните её 🙂

# Вывод:
# ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

# ['d', 'r', 'b', 'b', 'a', 'r', 'a', 'a', 'a', 'a', 'c']

import random

example = list('abracadabra')
print(example)
random.shuffle(example)
print(example)