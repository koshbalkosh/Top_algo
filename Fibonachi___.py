# Классическая задача, которую можно встретить на собеседованиях самого разного уровня. 
# Стоит напомнить, что последовательность Фибоначчи — это ряд чисел, где каждое последующее является суммой двух предыдущих.
# Так, первые десять чисел выглядят следующим образом: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

# Замкнутая формула

from __future__ import division
import math

def fib(n):
  SQRT5 = math.sqrt(5)
  PHI = (SQRT5 + 1) / 2
  return int(PHI ** n / SQRT5 + 0.5)
