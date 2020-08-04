n = int(input())
l = list(map(int, input().split()))
untreated = 0
currentoff = 0
for ele in l:
    if ele > 0:
        currentoff += ele
    else:
        if currentoff==0:
            untreated += 1
        else:
            currentoff -= 1
print(untreated)