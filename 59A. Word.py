s = input()
lc = 0
uc = 0
for ele in s:
    if ele >='a' and ele <='z':
        lc += 1
    elif ele >='A' and ele <='Z':
        uc += 1
if lc >= uc:
    print(s.lower())
else:
    print(s.upper())