def most_frequent(data):
    max=0
    for i in range(1,len(data)):
        if data.count(data[i])>data.count(data[max]) :
            max= i
    return data[max]

print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a']))