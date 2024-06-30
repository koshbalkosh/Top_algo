# 1. Способ 1

def is_anagram(str1, str2):
  # создаем словарь для первого слова
  dict1 = {}
  for char in str1:
    dict1[char] = dict1.get(char, 0) + 1
 
  # создаем словарь для второго слова
  dict2 = {}
  for char in str2:
    dict2[char] = dict2.get(char, 0) + 1
 
  # сравниваем словари
  return dict1 == dict2


# 2. Оптимизация алгоритма

def is_anagram(str1, str2):
  # создаем словарь для первого слова
  dict1 = {}
  for char in str1:
    dict1[char] = dict1.get(char, 0) + 1
 
  # проверяем второе слово
  for char in str2:
    if char in dict1:
      dict1[char] -= 1
      if dict1[char] == 0:
        del dict1[char]
    else:
      return False
 
  # если словарь пуст, значит слова являются анаграммами
  return not dict1
