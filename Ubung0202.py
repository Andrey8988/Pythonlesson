sps=[]
i=int(input("введите длину списка   "))
n=0
while n < i:
    x=input("введите элемент списка   ")
    sps.append(x)
   # print(sps)
    n += 1
print("сформированный список", sps)
sd=[]
k=0
while k < i:
    k2=k; k2 += 2
    sd.extend(sps[k:k2])
    sd.reverse()
   # print(sd)
    sps[k:k2]=sd
    sd=[]
    k += 2
print("Измененный список", sps)
