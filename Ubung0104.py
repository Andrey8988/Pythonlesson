ez=int(input('Schreiben die Zahl, bitte: '))
ez=str(ez)
i=len(ez)
gf=list(ez)
i=int(i)
nf=int(0)
print("Ziffern im Zahl - ",i)
sa=0
while i > nf:
    gf[nf] = int(gf[nf])
    if gf[nf] > sa:
        sa = gf[nf]
    nf += 1
print('Maximal Ziffer ist -',sa)
