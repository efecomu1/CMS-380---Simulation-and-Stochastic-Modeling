"""
Sprint 3 - Ticket Problem
Efe Comu
"""

import random


def simulate():

  # Empty seats initialization
  seats = [0] * 100
  # Assign seat 1 to passenger 1
  seats[0] = 1
  # Passengers 2 to 100
  for i in range(2, 101):
    assignedSeat = i - 1
    # Check if assigned seat is unoccupied
    if seats[assignedSeat - 1] == 0:
      seats[assignedSeat - 1] = i
      # If assigned seat is occupied, find another unoccupied seat
    else:
      emptySeats = []
      for j in range(100):
        if seats[j] == 0:
          emptySeats.append(j)
      currentSeat = random.choice(emptySeats)
      seats[currentSeat] = i
  # Checking if passenger 100 sits in her assigned seat
  if seats[99] == 100:
    return True
  else:
    return False


# Run the simulation for a large number of trials
trials = 1000
successes = 0
for i in range(trials):
  if simulate():
    successes += 1

# Estimated probability
probability = successes / trials

# Print the estimated probability
print("Probability that passenger 100 gets to sit in seat 100:", probability)
