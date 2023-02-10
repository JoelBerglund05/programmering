import random
import time
import sys

save = "2 3 6"
throw_li = ["2", "3", "5", "5", "6"]


answer = save.split(" ")
for number in answer:
  if number in throw_li:
    save = throw_li.pop(throw_li.index(number))
    throw_li.append(str(random.randint(1, 6)))
  else:
    save = input("Dessa tärnignar har du inte").lower()

print(throw_li)
