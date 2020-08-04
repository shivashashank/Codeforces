str1 = input()
count = 0
l = []
for ele in str1:
    if ele not in l:
        l.append(ele)
        count += 1
if count % 2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")