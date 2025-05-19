import random

c = 1000000
f = []

for i in range(c):
    f.append(random.randint(-10,5000))

print(sum(f) / c)
