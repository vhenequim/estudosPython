import random
from replit import clear
from art import logo

def deal_card():
  """Deals a card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def check_score(hand):
  """sum the score and checks if it's a blackjack"""
  if sum(hand) == 21:
    return 21
  if sum(hand) > 21 and 11 in hand:
    hand.remove(11)
    hand.append(1)
    print ("Ace!")
  return sum(hand)
  
def winner_checker(your_score, cpu_score):
  if your_score > 21 and cpu_score > 21:
    return "You have passed the limit. You lose"
  if your_score == cpu_score:
    return "You have drawed"
  elif cpu_score == 0:
    return "CPU got BlackJack, you lose"
  elif your_score == 0:
    return "You win!!!"
  elif your_score > 21:
    return "You have passed the limit. You lose"
  elif cpu_score > 21:
    return "CPU have passed the limit. You win"
  elif your_score > cpu_score:
    return "You win!!!"
  else:
    return "You lose"






def game():
  game_check = True
  your_hand = []
  cpu_hand = []
  for _ in range(2):
    your_hand.append(deal_card())
    cpu_hand.append(deal_card())
  while game_check:
    your_score = check_score(your_hand)
    cpu_score = check_score(cpu_hand)
    print (f"Your score: {your_score}")
    print (f"CPU score: {cpu_score}")
    if cpu_score == 21 or your_score == 21 or your_score > 21:
      game_check = False
    else:
      if input("Do you want do draw another card? 'y' or 'n'") == 'y':
        your_hand.append(deal_card())
      else:
        game_check = False
  while cpu_score != 21 and cpu_score < 17:
    cpu_hand.append(deal_card())
    cpu_score = check_score(cpu_hand)
  print (f"Your final score: {your_score}")
  print (f"CPU final score: {cpu_score}")
  print (winner_checker(your_score, cpu_score))








while input("Do you want to play? 'y' or 'n'") == "y":
  clear()
  game()
