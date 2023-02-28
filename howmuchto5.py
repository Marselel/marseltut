a = list(map(int,input().split()))
m = sum(a) / len(a)
q = m
s = 0
if m >= 4.5:
    print('ваш балл на 5 =', m)
    print('Its very good')
else:
    while q < 4.5:
        a.append(5)
        q = sum(a) / len(a)
        s += 1
    if s%10 == 1:
        print('Ваш балл ', round(m,2), 'вам нужно получить еще', s, 'пятерку чтоб ваш балл стал', q, 'на пятерку')
    elif s%10 == 2 or s%10 == 3 or s%10 == 4:
        print('Ваш балл ', round(m, 2), 'вам нужно получить еще', s, 'пятерки чтоб ваш балл стал', q, 'на пятерку')
    else:
        print('Ваш балл ', round(m, 2), 'вам нужно получить еще', s, 'пятерок чтоб ваш балл стал', q, 'на пятерку')
input()
