############### Blackjack Project #####################
from art import logo
import random
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0

def deal():
  #blank hands
  player_hand = []
  dealer_hand = []
  #deal cards
  player_hand.append(random.choice(cards))
  player_hand.append(random.choice(cards))
  dealer_hand.append(random.choice(cards))
  dealer_hand.append(random.choice(cards))
  #sets shown card
  dealer_shown_card = dealer_hand[0]
  #sets win and loss conditions to false
  player_blackjack = False
  dealer_blackjack = False
  player_bust = False
  dealer_bust = False
  #gets scores
  get_scores()
  #shows necessary info to choose hit or pass (shows cards)
  print(f"Your cards: {player_hand}, current score: {player_score}")
  print(f"Dealer's first card: {dealer_shown_card}")

def get_scores():
  #blanks scores
  player_score = 0
  dealer_score = 0
  #adds up cards one at a time from list (hands)
  for card in player_hand:
    player_score += card
  for card in dealer_hand:
    dealer_score += card

#end condition after make sure no bust or blackjack
def compare_score():
  #shows hands and scores
  print(f"Your final hand: {player_hand}, final score: {player_score}")
  print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
  #checks win and loss conditions
  if dealer_score == player_score:
    print("It's a draw. Unfortunately the dealer wins when there's a draw.")
    lose()
  elif dealer_score > player_score:
    lose()
  else:
    win()

def check_bust():
  if player_score > 21:
    player_bust = True
    should_continue = False
  elif dealer_score > 21:
    dealer_bust = True
    should_continue = False

def check_blackjack():
  if player_score == 21:
    player_blackjack = True
    should_continue = False
  elif dealer_score == 21:
    dealer_blackjack = True
    should_continue = False
  
def hit():
  should_hit = input("Type 'y' to get another card, type 'n' to pass: ")
  if should_hit == "y":
    player_hand.append(random.choice(cards))
  elif should_hit == "n":
    if dealer_score < 17:
      dealer_hand.append(random.choice(cards))
    else:
      should_continue = False

def win():
  print("You win!")
  play_blackjack()

def lose():
  print("You lose... Better luck next time!")
  play_blackjack()
    
def play_blackjack():
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play == "n":
    print("Goodbye.")
  elif play == "y":
    print(logo)
    deal()
#Transplant starts here
    should_continue = True
    check_blackjack()
    while should_continue:
      get_scores()
      check_bust()
      if should_continue:
        hit()
    if player_blackjack:
      print("You hit Blackjack!")
      win()
    elif dealer_blackjack:
      print("Dealer hit Blackjack.")
      lose()
    elif player_bust:
      print("You went over 21. You bust.")
      lose()
    elif dealer_bust:
      print("Dealer went over 21! The dealer busts!")
      win()
    else:
      compare_score()
  #Transplant ends here
  else:
    print("That wasn't a valid answer.")
    play_blackjack()

play_blackjack()