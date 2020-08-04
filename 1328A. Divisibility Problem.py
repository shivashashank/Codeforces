for _ in range(int(input())):
    a, b = map(int, input().split())
    moves = 0
    if a % b == 0:
        print(moves)
    else:
        print(b - (a % b))