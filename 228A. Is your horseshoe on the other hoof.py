c = list(map(int, input().split()))
l = []
 
for ele in c:
    if ele not in l:
        l.append(ele)
        
print(4-len(l))