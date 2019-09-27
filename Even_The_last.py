def checkio(array):
  sum=0
  if array!=[]:
    for i in range(len(array)):
        sum+=abs(i%2-1)*array[i]
    return sum*array[len(array)-1]
  else:
      return 0
print(checkio([0, 1, 2, 3, 4, 5]))
