def solution(n):
    if n == 1:
        return 0

    steps = 0

    while n > 1:
        if n == 3:
            return steps + 2
        elif not n % 2:
            n /= 2
        else:
            trailing1 = trailingZeros(n + 1)
            trailing2 = trailingZeros(n - 1)
            if trailing1 > trailing2:
                n = n + 1
            else:
                n = n - 1
        steps += 1

    return steps


def closestSquare(n):
    square = 2

    while square < n:
        square *= 2


def trailingZeros(n):
    count = 0

    while not n % 2:
        n = n >> 1
        count += 1

    return count


print(solution(15))
