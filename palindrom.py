# 1. Метод с использованием индексации

s = "radar"
if s == s[::-1]:
  print("Это палиндром")
else:
  print("Это не палиндром")


# 2. Метод с использованием цикла

s = "radar"
is_palindrome = True
for i in range(len(s) // 2):
  if s[i] != s[-i - 1]:
    is_palindrome = False
    break

if is_palindrome:
  print("Это палиндром")
else:
  print("Это не палиндром")
