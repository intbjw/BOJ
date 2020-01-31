import re
m = r'(\d+):(\d+):(\d+)'


def replace(m):
    data1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    data2 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    yy = eval(m.group(1))
    mm = eval(m.group(2))
    dd = eval(m.group(3))
    #return "{}年{}月{}日".format(yy, mm, dd)
    if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0):
        return str(data1[mm-1]+dd)
    else:
        return str(data2[mm-1]+dd)


n = eval(input())
for i in range(n):
    string = input()
    print(re.sub(m, replace, string))
