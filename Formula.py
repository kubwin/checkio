import math
def numberOfTrials(stdev, delta, q):
      return ((4 * stdev * stdev) / (delta * delta * q * (1 - q)))

print((math.sqrt(0.01*(1-0.01)))