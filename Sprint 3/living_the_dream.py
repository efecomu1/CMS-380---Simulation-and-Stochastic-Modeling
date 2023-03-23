"""
Sprint 3 - Dragon Dice Problem
Efe Comu
"""

from scipy.stats import poisson

# ChatGPT answering probability
p_automatic = 0.8

rate = 10

lambd = rate * 2

# Probability of personally answering more than 25 emails in 8 hours
p_final = poisson.pmf(0, lambd * (1 - p_automatic))
print(
  "Probability that I need to personally answer more than 25 e-mails in an eight hour workday: ",
  p_final)

# ------------------------------

# Expected number of emails in 2 hours
lambd_2 = rate * 8

# probability that I get no e-mails that must be personally answered in two hours
p_final_2 = poisson.pmf(range(26), lambd_2 * (1 - p_automatic))
print(
  "Probability that I get no e-mails that must be personally answered in two hours: ",
  1 - sum(p_final_2))
