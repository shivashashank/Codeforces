n = int(input())
count = 0
s = input()
for i in range(n-1):
    if s[i]==s[i+1]:
        count += 1
print(count)