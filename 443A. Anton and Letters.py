s = input()
s1 = s[1:-1]
l = list(s1.replace(', ', ''))
l1 = []
 
for ele in l:
    if ele not in l1:
        l1.append(ele)
        
print(len(l1))