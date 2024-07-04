# Необходимо реализовать функцию, принимающую в аргументах строку, состоящую из букв, и возвращающую новую строку, в которой повторяющиеся буквы заменены количеством повторений.


def encode_message(message):
  encoded_string = ""
  i = 0
  while (i <= len(message)-1):
    count = 1
    ch = message[i]
    j = i
    while (j < len(message)-1):
      if (message[j] == message[j + 1]): 
        count = count + 1
        j = j + 1
      else: 
        break
    encoded_string = encoded_string + str(count) + ch
    i = j + 1
  return encoded_string
