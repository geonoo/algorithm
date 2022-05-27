height = []
sum = 0
for h in height:
    sum += h
try:
    print(sum/len(height))
except ZeroDivisionError:
    print('응~ 0으로는 못 나눠~')