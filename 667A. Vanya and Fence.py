n, h = map(int, input().split())
hlist = list(map(int, input().split()))
width = 0
for ele in hlist:
    if ele > h:
        width += 2
    else:
        width += 1
print(width)