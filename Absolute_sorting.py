def checkio(numbers_array):
    a={}
    for i in range(len(numbers_array)):
          a[numbers_array[i]]=abs(numbers_array[i])
    a= sorted(a.items(), key=lambda item: item[1])
    return [a[i][0] for i in range(len(numbers_array))]


print(checkio((-20, -5, 10, 15)))