num = int(input())
while True:
    num += 1
    n = str(num)
    if (n[0] != n[1]) and (n[0] != n[2]) and (n[0] != n[3]) and (n[1] !=n[2]) and (n[1]!= n[3]) and (n[2] !=n[3]):
        break
print(num)