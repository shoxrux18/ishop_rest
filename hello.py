# N = int(input())
# f = int(input())

# for s in f:
#     f += s / N
    
# print(f)
# def __init__(self,name,age):
#     self.name = name
#     self.age = age

# sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
# fish = ['barracuda','cod','devil ray','eel']
# sea_creatures = fish.copy()
# print(sea_creatures)
# for x in range(1,4):
#     sea_creatures += ['fish']
#     print(sea_creatures)

# numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# print(numbers[1:11:2])
# a = int(input())
# print(False if a < 0 else a == int(str(a)[::-1]))
# lst = list(range(1,100))
# for f in lst:
#     lst.append(f)1
from math import ceil

n = int(input())
numbs = list(map(int, input().split()))
a, b = map(int, input().split())
m = min(numbs)

for i in range(n):
    if numbs[i] in numbs[a-1:b]:
        numbs[i] /= m

for numb in numbs:
    print(ceil(numb*10)/10, end=' ')
print()