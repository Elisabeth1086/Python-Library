# Криптографическая зашита генератора случайных данных
# Случайные числа, полученные при помощи модуля random в Питоне, не являются криптографически устойчивыми. 
# Это означает, что криптоанализ позволяет предсказать какое число будет сгенерировано следующим. Попробуем исправить ситуацию.

# Модуль secrets используется для генерации криптографически сильных случайных чисел, пригодных для управления данными , такими как пароли, 
# аутентификации учетной записи, маркеры безопасности и так далее.

# Его зачастую следует использовать вместо генератора псевдослучайных чисел по умолчанию в модуле random, 
# который предназначен для моделирования и симуляции, а не безопасности или криптографии.

# Вывод:
# 3
# 4
# 48
# [48, 42, 24]
# 16.43293639196964

import secrets

secretsGenerator = secrets.SystemRandom()
random_number = secretsGenerator.randint(0, 50)
print(random_number)

random_number2 = secretsGenerator.randrange(4, 40, 4)
print(random_number2)

number_list = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
secure_choice = secretsGenerator.choice(number_list)
print(secure_choice)

secure_sample = secretsGenerator.sample(number_list, 3)
print(secure_sample)

secure_float = secretsGenerator.uniform(2.5, 25.5)
print(secure_float)