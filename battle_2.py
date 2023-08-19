def max_min(a=[]):
    max = a[0]
    min = a[0]
    for i in range(len(a)-1):
        max = a[i]
        for j in range(i, len(a)):
            if a[j] > a[i]:
                max = a[j]

    for c in range(len(a)-1):
        min = a[c]
        for d in range(i, len(a)):
            if a[d] < a[c]:
                min = a[d]
    print(f"Nonb ki pi gran an se {max}")
    print(f"Nonb ki pi piti a se {min}")
    
    

lis = [18, 26, 78, 56, 19, 40, 1, 100]

max_min(lis)