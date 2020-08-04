n = int(input())
s = input().lower()
count = 0
a = []
for ele in s:
    if ele not in a:
        a.append(ele)
        
if len(a) == 26:
    print("YES")
else:
    print("NO")