s = input().lower()
t = input().lower()
if s == t[::-1]:
    print('YES')
else:
    print('NO')