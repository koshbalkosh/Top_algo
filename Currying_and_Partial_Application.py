# Каррирование — это преобразование функции от многих аргументов в набор функций, каждая из которых является функцией от одного аргумента. 
# Мы можем передать часть аргументов в функцию и получить обратно функцию, ожидающую остальные аргументы.

# Создадим простую функцию greet, которая принимает в качестве аргументов приветствие и имя:

def greet(greeting, name):
  print(greeting + ', ' + name)

# Небольшое улучшение позволит нам создать новую функцию для любого типа приветствия и передать этой новой функции имя:

def greet_curried(greeting):
  def greet(name):
    print(greeting + ', ' + name)
  return greet

greet_hello = greet_curried('Hello')

greet_hello('German')
greet_hello('Ivan')

# или напрямую greet_curried
greet_curried('Hi')('Roma')

# А дальше можно сделать это с любым количеством аргументов:

def greet_deeply_curried(greeting):
  def w_separator(separator):
    def w_emphasis(emphasis):
      def w_name(name):
        print(greeting + separator + name + emphasis)
      return w_name
    return w_emphasis
  return w_separator

greet = greet_deeply_curried("Hello")("...")(".")
greet('German')
greet('Ivan')

# Или вариант с lambda:

