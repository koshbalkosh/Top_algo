# Метод двух указателей является эффективным подходом для решения ряда задач на Python и не только. 
# Он заключается в использовании двух указателей, которые движутся по структуре данных в разных направлениях или с разной скоростью.


left, right = 0, len(nums) - 1
while left < right:
  if nums[left] + nums[right] == target:
    return [left + 1, right + 1]
  elif nums[left] + nums[right] < target:
    left += 1
  else:
    right -= 1
