cost, dollors, wants  = map(int, input().split())
sum = 0
for i in range(1, wants+1):
   sum += cost*i
if dollors - sum > 0:
    print('0')
else:
    print(sum-dollors)