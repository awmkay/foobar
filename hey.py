def solution(n, b):
    num_list = []

    recursiveSol(n, b, num_list)
    lastNum = len(num_list) - 1
    return lastNum - num_list.index(num_list[lastNum])


def recursiveSol(n, b, num_list):
    num_list.append(n)

    k = len(n)
    d = {}
    for num in n:
        if num not in d:
            d[int(num)] = n.count(num)

    y = ''
    while d:
        key = min(d)
        y += str(key) * d[key]
        del d[key]
    x = int(y[::-1], b)
    y = int(y, b)

    z = decToB(x - y, b).zfill(k)
    if z in num_list:
        num_list.append(z)
    else:
        recursiveSol(z, b, num_list)


def decToB(num, b):
    convertString = "0123456789ABCDEF"
    if num < b:
        return convertString[num]
    else:
        return decToB(num // b, b) + convertString[num % b]


print(solution('122221', 3))
