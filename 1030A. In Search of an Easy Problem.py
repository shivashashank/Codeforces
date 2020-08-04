n = int(input())
prbls = list(map(int, input().split()))
diff = 'EASY'
for ele in prbls:
    if ele == 1:
        diff = 'HARD'
print(diff)