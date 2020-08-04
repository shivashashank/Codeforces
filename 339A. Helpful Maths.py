s1 = input()
l1 = []
for i in range(1,len(s1)+1):
    if i%2==1:
        l1.append(s1[i-1])
        
l1 = sorted(l1)
l2 = []
for i in range(len(l1)):
    l2.append(l1[i])
    l2.append('+')
print(''.join(l2[:-1]))