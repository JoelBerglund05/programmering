import random

def vinst_lucka():
  lucka = random.randint(0, 2)

  luckor.insert(lucka, 1)

  tabort = luckor.pop(3)

try_again = True

while try_again:
  start = input("vill du spela?").lower() 
  if start == 'ja':
    try_again = False 

while start == "ja":
  luckor = [0, 0, 0]
  vinst_lucka()

  try_again = True
  while try_again:
    lucka_val = input("vilken lucka väljer du? 1-3").lower()
    if lucka_val == "1" or lucka_val == "2" or lucka_val == "3":
      lucka_val = int(lucka_val) - 1
      luckor.insert(lucka_val, 2)
      tabort = luckor.pop(lucka_val + 1)
      e = False

  print("Lucka", luckor.index(0) + 1, "öppnas, den är tom")
  luckor.insert(luckor.index(0), 3)
  öppen_lucka = luckor.pop(luckor.index(0))

  i = True 
  while i == True:
    lucka_val_ja_nej = input("Vill du byta lucka?").lower()
    if lucka_val_ja_nej == "ja":
      if tabort != 1:
        print("Grattis! Du vann!")
        i = False
      else:
        print("ledsen du förlorade")
        i = False
    elif lucka_val_ja_nej == "nej":
      if tabort == 1:
        print("Grattis! Du vann!")
  
        i = False
      else:
        print("ledsen du förlorade")
        i = False

  i = True
  while i:
    start = input("vill du spela vidare?").lower()
    if start == 'ja':
      i = False