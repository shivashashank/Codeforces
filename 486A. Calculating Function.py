n = int(input())
sum = 0
if n %2 == 0:
    sum = n//2
else:
    sum = (n//2+1)*-1
print(sum)