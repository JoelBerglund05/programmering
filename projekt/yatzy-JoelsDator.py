import random
import time
import sys


#greeting and  question if the game should begin

print("Välkommen till Yatzy spelet!")
time.sleep(1)
play = input("vill du börja spela?").lower()

#general game options wich needs to be answerd before the game starts

while play != "ja" and play != "nej":
  play = input("något blev fel testa en gågn till. Vill du börja spela?")

if play == "ja":
  players = input("Hur många spelare ska vara med? det kan max vara fyra spelare och minst två.")
elif play == "nej":
  print("välkommen åter")
  sys.exit()

#(general game options) Player count restriction

if players != "1" and players != "2" and players != "3" and players != "4":
  players = input("något blev fel testa en gågn till. Hur många spelar ska vara med?")

#(general game options) Create players

#variables

playercount =[]
playercounter = 0
player_li = []


#(general game options) creation of players

for i in players:
  if i == "2":
    player_li.append(input("vad ska spelare 1 heta?"))
    player_li.append(input("vad ska spelare 2 heta?"))
    print("välkomna", player_li[0], "och", player_li[1])
  elif i == "3":
    player_li.append(input("vad ska spelare 1 heta?"))
    player_li.append(input("vad ska spelare 2 heta?"))
    player_li.append(input("vad ska spelare 3 heta?"))
    print("välkomna", player_li[0]+ ",", player_li[1], "och", player_li[2])
  elif i == "4":
    player_li.append(input("vad ska spelare 1 heta?"))
    player_li.append(input("vad ska spelare 2 heta?"))
    player_li.append(input("vad ska spelare 3 heta?"))
    player_li.append(input("vad ska spelare 4 heta?"))
    print("välkomna", player_li[0]+ ",", player_li[1]+ ",", player_li[2], "och", player_li[3])

#Game

#variables

throw_li = []
combination = ["ettor", "tvåor", "treor", "fyror", "femor", "sexor", "1par", "2par", "tretal", "fyrtal", "liten stege", "stor stege", "kåk", "chans", "yatzy"]

#definitions

def randomizer():
  for i in range(5):
    dice = random.randint(1, 6)
    throw_li.append(str(dice))
  
#(definitions) retry to get combination

def choose():
  save = input("vilka tärningar vill du slå om?").lower()
  answer = save.split(" ")
  for number in answer:
    if number in throw_li:
      save = throw_li.pop(throw_li.index(number))
      throw_li.append(str(random.randint(1, 6)))
    else:
      save = input("Dessa tärnignar har du inte").lower()

#enter game

while play == "ja":
  #game randomizer

  randomizer()

  for i in range(3):
    #turn player1

    print(player_li[0] + "s", "tur")
    print("Tärningarna blev", throw_li)
    time.sleep(1)
    print("Du har dessa kombinationer att välja mellan", combination)

    choose()
  throw_li.clear()