# Мемоизация - это метод, используемый для хранения результатов предыдущих вызовов функций для ускорения будущих вычислений. 
# Если повторные вызовы функций выполняются с одинаковыми параметрами, мы можем сохранить предыдущие значения вместо повторения ненужных вычислений. 


def factorial(input_value):
  if input_value < 2:
    return 1
  elif input_value >= 2:
    return input_value * factorial(input_value - 1)

# Теперь попробуем многократно воспользоваться этой функцией с помощью цикла:

for i in range(1, 11):
  print(f"{i}! = ", factorial(i))

# Теперь давайте пройдемся по этапам реализации метода мемоизации. Чтобы продолжить, давайте инициализируем словарь:

factorial_dict = {}

# Далее мы определим нашу функцию с применением мемоизации. Сначала мы проверяем, меньше ли введенное значение 2, и возвращаем 1, если это так:

def factorial_memo(input_value):
  if input_value < 2:
    return 1

# Затем мы проверяем, есть ли входное значение в словаре. Если это не так, мы сохраняем значение факториала в словаре и возвращаем значение для ключа ввода. Полная функция выглядит так:

def factorial_memo(input_value):
  if input_value < 2:
    return 1
  if input_value not in factorial_dict:
    factorial_dict[input_value] = input_value * factorial_memo(input_value - 1)
  return factorial_dict[input_value]

# Эта функция уже способна осилить наш цикл в 5000 итераций, но мы могли бы поступить иначе.
# А именно, импортировать декоратор из модуля functools, называемого lru_cache, который позволяет нам кэшировать наши значения. 
# Мы можем достичь той же производительности, что и с нашим методом factorial_memo, используя этот декоратор:

from functools import lru_cache

@lru_cache(maxsize = 1000)
def factorial(input_value):
  if input_value < 2:
    return 1
  elif input_value >= 2:
    return input_value * factorial(input_value - 1)
