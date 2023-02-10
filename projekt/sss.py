import random

save = "2 3 6"
throw_li = ["2", "3", "5", "5", "6"]


answer = save.split(" ")
for number in answer:
  if number in throw_li:
    throw_li.remove(number)
    while len(throw_li) < 5:
      dice = random.randint(1, 6)
      throw_li.append(str(dice))
  else:
    save = input("Dessa tärnignar har du inte").lower()

print(throw_li)

print(type(True))
