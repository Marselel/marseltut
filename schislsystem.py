fs=int(input('Входная система счисления:'))
ls=int(input('Выходная система счисления:'))
a = int(input('Число:'))


def bigtosmall(a):
    r = []
    k = 0
    while a >= ls:
        r.append(a % ls)
        a = a // ls
    r.append(a)
    d = r[::-1]
    for i in d:
        k += i * (10 ** (r.index(i)))
        r[r.index(i)] = ''
    return k

def smalltobig(a):
    r=0
    a = [int(i)for i in str(a)][::-1]
    for i in a:
        d = a.index(i)
        r+=i*(fs**d)
        a[d]=' '

    return r


if fs<ls and ls==10:
    a = smalltobig(a)
elif fs>ls and fs ==10:
    a=bigtosmall(a)
elif fs<ls and ls !=10 or fs>ls and ls !=10:
    a = smalltobig(a)
    a = bigtosmall(a)
print(a)
input()
# код написан Истяковым Марселем