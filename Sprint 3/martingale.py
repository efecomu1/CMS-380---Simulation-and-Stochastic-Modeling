"""
Sprint 3 - Martingale Problem
Efe Comu
"""

import random
import matplotlib.pyplot as plt


def simulate(st_Bet, st_Bankroll, maxSpins, maxLossStreak):
  bankroll = st_Bankroll
  bet = st_Bet
  spins = 0
  netgain = 0
  lossStreak = 0

  while spins < maxSpins and bet <= bankroll:
    result = random.choice(['red', 'black'])

    if result == 'black':
      bankroll += bet
      netgain += bet
      bet = st_Bet
      lossStreak = 0

    else:
      bankroll -= bet
      netgain -= bet
      bet *= 2
      lossStreak += 1
      if lossStreak >= maxLossStreak:
        break
    spins += 1

  return netgain


st_Bet = 1
st_Bankroll = 255
maxSpins = 100
maxLossStreak = 8

gameResults = []
for i in range(1000):
  finalBankroll = simulate(st_Bet, st_Bankroll, maxSpins, maxLossStreak)
  gameResults.append(finalBankroll)

plt.figure()
plt.hist(gameResults, 20)
plt.title("Game Results Histogram")
plt.xlabel("Net Gain of Bankroll")
plt.ylabel("Count")
plt.savefig('hist.png', bbox_inches='tight')
