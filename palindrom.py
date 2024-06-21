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


# 3. Использование функции

def is_palindrome(s):
  if len(s) < 2:
    return True
  if s[0] != s[-1]:
    return False
  return is_palindrome(s[1:-1])


# 4. Определение палиндрома с учетом пробелов и знаков препинания

s = "A man, a plan, a canal: Panama"
s = ''.join(c for c in s if c.isalnum()).lower()
if s == s[::-1]:
  print("Это палиндром")
else:
  print("Это не палиндром")
