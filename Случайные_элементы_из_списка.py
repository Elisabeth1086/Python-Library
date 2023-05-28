# Случайные элементы из списка — choices()
# random.choices делает то же, что и random.sample(), но элементы, которые она возвращает, могут быть не уникальными.

# Вывод:
# ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']

# ['d', 'a', 'd', 'a', 'r', 'b', 'r', 'a', 'd', 'b', 'a', 'r', 'd', 'a', 'a']

import random

example = list('abracadabra')
print(example)
print(random.choices(example, k=15))