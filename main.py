############### Blackjack Project #####################
from art import logo
import random
from replit import clear

def deal():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  #checks for Blackjack
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #check for ace and change from 11 to 1 if would bust otherwise
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare_score(player_score, dealer_score):
  #bug fix if over and equal
  if player_score > 21 and dealer_score > 21:
    return "You went over. You lose."
  if dealer_score == player_score:
    return "Draw. Dealer wins when there's a draw. You lose."
  elif dealer_score == 0:
    return "Dealer has Blackjack. You lose."
  elif player_score == 0:
    return "You have Blackjack! You win!"
  elif player_score > 21:
    return "You went over. Bust. You lose."
  elif dealer_score > 21:
    return "Dealer went over. Bust. You win!"
  elif player_score > dealer_score:
    return "You win!"
  else:
    return "You lose."   
  
def play_blackjack():
  print(logo)
  player_hand = []
  dealer_hand = []
  should_continue = True

  #deal 2 cards each
  for _ in range(2):
    player_hand.append(deal())
    dealer_hand.append(deal())

  #loop to actually play
  while should_continue:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    #stops game if blackjack or bust
    if player_score == 0 or dealer_score == 0 or player_score > 21:
      should_continue = False
    else:
      hit = input("Type 'y' to get another card, type 'n' to pass: ")
      if hit == "y":
        player_hand.append(deal())
      else:
        should_continue = False

  #makes dealer hit if 16 or below and hasn't busted
  while dealer_score != 0 and dealer_score < 17:
    dealer_hand.append(deal())
    dealer_score = calculate_score(dealer_hand)

  print(f"   Your final hand: {player_hand}, final score: {player_score}")
  print(f"   Computer's final hand: {dealer_hand}, final score: {dealer_score}")
  print(compare_score(player_score, dealer_score))

#plays game until choose not to
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_blackjack()