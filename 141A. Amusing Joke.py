a = input().lower()
b = input().lower()
c = input().lower()
la = list(a)
lb = list(b)
lc = list(c)
l = []
for ele in la:
    l.append(ele)
for ele in lb:
    l.append(ele)
 
l.sort()
lc.sort()
 
if l == lc:
    print('YES')
else:
    print('NO')