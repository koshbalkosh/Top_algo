# Подсчёт гласных в строке

string = "Привет, мир!"
count = 0

for char in string:
  if char in "аеёиоуыэюяАЕЁИОУЫЭЮЯ":
    count += 1

print("Количество гласных букв:", count)
