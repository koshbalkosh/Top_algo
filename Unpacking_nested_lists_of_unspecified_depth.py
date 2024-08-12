# Распаковка вложенных списков неопределенной глубины


# Задача
# Напишите функцию flatten, которая будет принимать на вход список с любой вложенностью (список в списке), 
# а возвращать список, где вложенные элементы всех уровней распакованы, то есть вложенное превращается в плоское.

# Варианты решения:

# Вариант 1:

def flatten(array: Iterable) -> List:
  new_array = array[:]
  ind = 0
  while True:
    try:
      while isinstance(new_array[ind], list):
        item = new_array.pop(ind)
        for inner_item in reversed(item):
          new_array.insert(ind, inner_item)
      ind += 1
    except IndexError:
      break
  return new_array


