n = eval(input())
for i in range(n):
    m = eval(input())
    s = ''
    while m:
        temp = m % 2
        s = s + str(temp)
        m = m // 2
    s = s[::-1]
    print(s)
