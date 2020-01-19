n = eval(input())
for _ in range(n):
    m = eval(input())
    l = [eval(x) for x in input().split()]
    o = 0
    j = 0
    for c in l:
        if c % 2 == 0:
            o = o + c
        else:
            j = j + c
    print(j, o)
