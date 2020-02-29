k=x=5
y=-5
def my_func(a,b):
    a=(a*k)
    global c
    c=1/a
    return a
n=-1
while n > y:
    x=my_func(x,y)
    n -= 1
print(k, "в степени", y, "равно", c)
