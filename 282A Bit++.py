x = 0
for i in range(int(input())):
    a = input()
    if(a[0:2] == "++" and a[-1] == "X") or (a[0] == "X" and a[1:3] == "++"):
        x += 1
    elif(a[0:2] == "--" and a[-1] == "X") or (a[0] == "X" and a[1:3] == "--"):
        x -= 1
print(x)
