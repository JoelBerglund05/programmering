point = [0]

def look_if_yes():
  e = False
      
  while e == False:
    if save == "ja":
      point[0] += combination_try[0] * 2
      combination_try.clear()
      print(point)
      return()
    elif save == "nej":
      e = True
    else:
      save = input("Någor blev fel. Ville du ha 1par?").lower()
  
  

def combination_look_up():
  combination_try = []
  stop2 = 0
  stop3 = 0

  #1par

  for i in throw_li:
    save = throw_li.count(i)
    

    if save >= 2:
      if len(combination_try) > 0:
        save = combination_try.pop(0)
        combination_try.append(int(i))
      else:
        combination_try.append(int(i))
    
    if i == throw_li[4] and len(combination_try) == 1:
      print(throw_li)
      save = input("Du har ett 1par vill du sätta in ditt tal som 1 par?").lower()
    
    look_if_yes()

    if e == True:
      break

  #2par

  for i in throw_li:
    save = throw_li.count(i)

    if save >= 2:
      combination_try = save.append(i)
    
        

    #if save == "ja":
      #point[0] += 

      #kåk

    if save == 2 and stop2 == 0:
      stop2 += 1
      combination_try.append(int(i))
    elif save == 3 and stop3 == 0:
      stop3 += 1
      combination_try.append(int(i))
    if len(combination_try) == 2:
      print(throw_li)
      save = input("du har en kåk vill du ta poängen till kåken?").lower()
      if save == "ja":
        point[0] += combination_try[0] * 2 + combination_try[1] * 3
        combination_try.clear()
        print(point)
        return()

        

throw_li =["5", "6", "6", "6", "5"]

combination_look_up()