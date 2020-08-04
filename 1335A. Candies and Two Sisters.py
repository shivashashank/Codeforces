for _ in range(int(input())):
    n = int(input())
    count = 0
    if n > 2:
        if n % 2 == 0:
            print(n//2-1)
        else:
            print(n//2)
    else:
        print(0)