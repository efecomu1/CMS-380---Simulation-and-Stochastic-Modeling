"""
Baccarat Class Notes
use randint(1, 13) to simulate drawing a card

There are two possible bets: Player and Banker

Start by testing whether the player hand wins
You can then test whether the Banker hand wins

simulate() method runs one round of Baccarat and returns the result
the loop at the end runs the game x many times and returns the winning percentages

Efe COMU
"""

from random import randint


def simulate():
  """
  Simulation of one round of the Baccarat game
  player win = return 1
  banker win = return 2
  tie game = return 3
  """
  # Card Generators
  CardOnePlayer = randint(1, 13)
  CardTwoPlayer = randint(1, 13)
  playerPoints = 0

  CardOneBanker = randint(1, 13)
  CardTwoBanker = randint(1, 13)
  bankerPoints = 0

  # Calculating player points after distribution
  if (CardOnePlayer < 10) and (CardTwoPlayer < 10):
    playerPoints = (CardOnePlayer + CardTwoPlayer) % 10
  elif (CardOnePlayer < 10) and (CardTwoPlayer > 10):
    playerPoints = CardOnePlayer % 10
  elif (CardOnePlayer > 10) and (CardTwoPlayer < 10):
    playerPoints = CardTwoPlayer % 10

  # Calculating banker points after distribution
  if (CardOneBanker < 10) and (CardTwoBanker < 10):
    bankerPoints = (CardOneBanker + CardTwoBanker) % 10
  elif (CardOneBanker < 10) and (CardTwoBanker > 10):
    bankerPoints = CardOneBanker % 10
  elif (CardOneBanker > 10) and (CardTwoBanker < 10):
    bankerPoints = CardTwoBanker % 10

  # Checking if there's a natural win or a tie
  if (playerPoints >= 8) and (bankerPoints >= 8):
    return 3
  elif (playerPoints >= 8) and (bankerPoints < 8):
    return 1
  elif (playerPoints < 8) and (bankerPoints >= 8):
    return 2

  # playerPoints between 0-5
  if (playerPoints <= 5):
    CardThreePlayer = randint(1, 13)
    if (CardThreePlayer <= 9):
      playerPoints += CardThreePlayer

    if (bankerPoints <= 2):
      CardThreeBanker = randint(1, 13)
      if (CardThreeBanker <= 9):
        bankerPoints += CardThreeBanker

    elif (bankerPoints == 3):
      if (CardThreePlayer != 8):
        CardThreeBanker = randint(1, 13)
        if (CardThreeBanker <= 9):
          bankerPoints += CardThreeBanker

    elif (bankerPoints == 4):
      if (CardThreePlayer >= 2 and CardThreePlayer <= 7):
        CardThreeBanker = randint(1, 13)
        if (CardThreeBanker <= 9):
          bankerPoints += CardThreeBanker

    elif (bankerPoints == 5):
      if (CardThreePlayer >= 4 and CardThreePlayer <= 7):
        CardThreeBanker = randint(1, 13)
        if (CardThreeBanker <= 9):
          bankerPoints += CardThreeBanker

    elif (bankerPoints == 6):
      if (CardThreePlayer >= 6 and CardThreePlayer <= 7):
        CardThreeBanker = randint(1, 13)
        if (CardThreeBanker <= 9):
          bankerPoints += CardThreeBanker

  elif (playerPoints > 5):
    if (bankerPoints <= 5):
      bankerCardThree = randint(1, 13)
      if (bankerCardThree <= 9):
        bankerPoints = bankerPoints + bankerCardThree

  # Score calculation
  if (playerPoints > bankerPoints):
    return 1
  elif (playerPoints < bankerPoints):
    return 2
  elif (playerPoints == bankerPoints):
    return 3


numGames = 100000
playerWins = 0
bankerWins = 0
ties = 0

# playing Baccarat numGames times
for x in range(numGames):
  result = simulate()
  if (result == 1):
    playerWins += 1
  elif (result == 2):
    bankerWins += 1
  elif (result == 3):
    ties += 1

playerFraction = (playerWins / numGames) * 100
bankerFraction = (bankerWins / numGames) * 100
tieFraction = (ties / numGames) * 100

print("Player Win Percentage: %.2f" % playerFraction + "%")
print("Banker Win Percentage: %.2f" % bankerFraction + "%")
print("Tie Percentage: %.2f" % tieFraction + "%")
