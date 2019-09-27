
def bigger_price(limit, data):
  Enddata = []
  max=data[0]["price"]
  maxI=0
  for i in range(limit):
        for j in range(len(data)):
           if data[j]["price"]>max :
                max=data[j]["price"]
                maxI=j
        Enddata.append(data[maxI])
        data.pop(maxI)
        max = data[0]["price"]
        maxI = 0
  return Enddata

print(bigger_price(2, [{"name": "bread", "price": 1000}, {"name": "wine", "price": 138}, {"name": "meat", "price": 15},
                       {"name": "water", "price": 1}]))

#def bigger_price(limit, data):                                               realrzacij boga
 #   data.sort(key=lambda food: food["price"])
 #   return [data.pop() for i in range(limit)]
'''def bigger_price(limit, data):
    data.sort(key=lambda food: food["price"])
    return [data.pop() for i in range(limit)]
print(bigger_price(2, [{"name": "bread", "price": 100}, {"name": "wine", "price": 138}, {"name": "meat", "price": 15},
                       {"name": "water", "price": 1}]))'''