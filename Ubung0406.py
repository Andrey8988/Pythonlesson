import itertools
for i in itertools.count(10):
    if i > 50: break
    print(i, end=" ")
n=1
for i in itertools.cycle("asda"):
    if n > 20: break
    print(i, end=" ")
    n += 1