import random 
import time
import sys

blah = "Welcome to Texas Hold Em"
for l in blah:
  sys.stdout.write(l)
  sys.stdout.flush()
  time.sleep(0.05)

print()
pot = 2000

#cardtype
jack = 11
queen = 12
king = 13
ace = 14

player_balance = 2000


#print(random)

suit_dictionary = {
  1: "spades",
  2: "diamonds",
  3: "hearts",
  4: "clubs"
}

card_dictionary = {
  1: "One",
  2: "Two",
  3: "Three",
  4: "Four",
  5: "Five",
  6: "Six",
  7: "Seven",
  8: "Eight",
  9: "Nine",
  10: "Ten",
  11: "Jack",
  12: "Queen",
  13: "King",
  14: "Ace",
}

print()

time.sleep(0.5)

print("Your cards are")

time.sleep(1)
card1 = ""

card2 = ""

for i in range(2):
  random_suit = random.randint(1, 4)

  random_card = random.randint(1, 14)

  if i == 0:
    card1 = card_dictionary[random_card] + " of " + suit_dictionary[random_suit]

  elif i == 1:
    card2 = card_dictionary[random_card] + " of " + suit_dictionary[random_suit]

print(card1)
print(card2)

time.sleep(1)

print()

print("The starting bid is 40 dollars")

time.sleep(0.5)
print("")
user_input = input("Do you want to call, fold, or raise?\n").lower()

if user_input == "call":
  player_balance = player_balance - 40
  print(f"Your balance is now {player_balance}")
  random_bet = random.randint(1, 300)


elif user_input == "raise":
  
  print()
  bet_amount = input("What amount do you want to bet?\n")
  random_bet = random.randint(int(bet_amount), 300)

  player_balance = player_balance - int(bet_amount)

  print(player_balance)

  players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

  ai_actions = ["fold", "bet", "call"]

  folded_list = []

  for player in players:

    time.sleep(1)
    cool = random.choice(ai_actions)
    
    if cool == "bet":
      total_generator = int(random_bet) + 1
      random_bet = random.randint(int(total_generator), 300)
      print(f"{player} raised the call to {total_generator}")

    elif cool == "call":
      print(f"{player} chose to call")

    elif cool == "fold":
      print(f"{player} chose to fold")
      index = players.index(player)
      folded_list.append(player)
      

  for folded_player in folded_list:
    players.remove(folded_player)
  

elif user_input == "fold":
  print()
  print("You will no longer be able to play for the rest of the round")
  random_bet = random.randint(1, 300)
  print()


players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

ai_actions = ["fold", "bet", "call"]

folded_list = []

if user_input == "call" or user_input == "fold":
  for player in players:

      time.sleep(1)
      cool = random.choice(ai_actions)
      
      if cool == "bet":
        total_generator = int(random_bet) + 1
        random_bet = random.randint(int(total_generator), 300)
        print(f"{player} raised the call to {total_generator}")

      elif cool == "call":
        print(f"{player} chose to call")

      elif cool == "fold":
        print(f"{player} chose to fold")
        index = players.index(player)
        folded_list.append(player)

  for folded_player in folded_list:
    players.remove(folded_player)
    
  

player_1_balance = "2000"



print()
print("The three cards in the middle are:")

for i in range(3):
  random_suit = random.randint(1, 4)
  random_card = random.randint(1, 14)

  if i == 0:
    middle_card1 = card_dictionary[random_card] + " of " + suit_dictionary[random_suit]

  elif i == 1:
    middle_card2 = card_dictionary[random_card] + " of " + suit_dictionary[random_suit]
  
  elif i == 2:
    middle_card3 = card_dictionary[random_card] + " of " + suit_dictionary[random_suit]

print(middle_card1)
print(middle_card2)
print(middle_card3)


user_card_list = [card1, card2]

middle_card_list = [middle_card1, middle_card2, middle_card3]

returnMatches = set(user_card_list) & set(middle_card_list)

if len(returnMatches) > 0:
  print("You Have a Match!")

#print(returnMatches)




  












