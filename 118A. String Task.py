s = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for ele in s:
    if ele in vowels:
        continue
    else:
        print('.'+ele, end = '')