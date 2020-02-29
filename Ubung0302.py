a=str("иванов ")
b=str("петя ")
c=str("22.02.2000 ")
d=str ("москва ")
e=str("ggg@if.com ")
f=str(2002555)
def funk(first_name=a, last_name=b, birth=c, city=d, email=e, tel=f):
    return first_name+last_name+birth+city+email+tel
print(funk())
