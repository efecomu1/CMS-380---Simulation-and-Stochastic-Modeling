import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('Agg')

# Add code here to open the file
f = open('data.txt', 'r')

# Declare an empty list
values = []

for line in f:
  line = line.strip()  # Remove whitespace

  # Cast to a float and then append to the list
  values.append(float(line))


# Now you calculate answers using the values list
def mean(x):
  """
    Calculate and return the mean of input list x
    """

  return sum(x) / len(x)


def median(x):
  """
    Calculate and return the median of input list x
    """
  x.sort()
  if len(x) % 2 == 1:
    mid = int((len(x) / 2))
    return x[mid]
  else:
    mid1 = int(len(x) / 2 - 1)
    mid2 = int(len(x) / 2)
    return (x[mid1] + x[mid2]) / 2


def variance(x):
  count = 0
  mean = sum(x) / len(x)
  for line in x:
    temp = mean - line
    count += temp * temp

  return count / len(x)


def st_deviation(x):
  ## variance(x)**(1 / 2)
  count = 0
  mean = sum(x) / len(x)
  for line in x:
    temp = mean - line
    count += temp * temp

  var = count / len(x)
  return var**(1 / 2)


## Main
## test = [1, 2, 4, 6, 7]

calc_mean = mean(values)
calc_median = median(values)
calc_variance = variance(values)
calc_stdev = st_deviation(values)

print(calc_mean)
print(calc_median)
print(calc_variance)
print(calc_stdev)

plt.figure()
plt.hist(values, 20)
plt.title('20-Bin Histogram')
plt.xlabel('Data value')
plt.ylabel('Count')
plt.savefig('histogram.png', bbox_inches='tight')

plt.figure()
plt.boxplot(values)
plt.title('Box-Plot')
plt.xlabel('Data value')
plt.ylabel('Count')
plt.savefig('boxplot.png', bbox_inches='tight')

plt.close()
