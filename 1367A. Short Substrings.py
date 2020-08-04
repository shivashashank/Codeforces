for _ in range(int(input())):
    a = input().lower()
    b = ''
    if len(a)==2:
        b = a
    elif len(a)>2:
        b += a[0]+a[1:-1:2]+a[-1]
    print(b)