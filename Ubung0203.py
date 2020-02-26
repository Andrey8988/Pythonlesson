i=int(input("введите номер месяца   "))
sl={
    1:"winter",
    2: "winter",
    12: "winter",
    3:"fruhling",
    4:"fruhling",
    5:"fruhling",
    6:"sommer",
    7:"sommer",
    8:"sommer",
    9:"herbst",
    10:'herbst',
    11:'herbst'}
if i in sl:
    print(sl.get(i))
else:
    print("Was ist das?")
