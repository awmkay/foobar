from fractions import Fraction


def solution(dimensions, your_position, guard_position, distance):
    maxBoxes = [int((distance / dimensions[i] / 2) + 1) for i in range(2)]
    gPosMirror = 0

    gFromR = dimensions[0] - guard_position[0]
    gFromL = guard_position[0]
    gFromT = dimensions[1] - guard_position[1]
    gFromB = guard_position[1]

    yFromR = dimensions[0] - your_position[0]
    yFromL = your_position[0]
    yFromT = dimensions[1] - your_position[1]
    yFromB = your_position[1]

    try:
        ygGrad = Fraction(gFromB - yFromB, gFromL - yFromL)
    except ZeroDivisionError:
        ygGrad = float("inf")

    for x in range(-maxBoxes[0], maxBoxes[0] + 1):
        for y in range(-maxBoxes[1], maxBoxes[1] + 1):
            try:
                if Fraction(y - yFromB, x - yFromL) == ygGrad:
                    continue
            except ZeroDivisionError:
                if ygGrad == float("inf"):
                    continue

            if x % 2:
                xG = x * dimensions[0] + gFromR
            else:
                xG = x * dimensions[0] + gFromL

            if y % 2:
                yG = y * dimensions[1] + gFromT
            else:
                yG = y * dimensions[1] + gFromB

            if (xG - yFromL) ** 2 + (yG - yFromB) ** 2 < distance ** 2:
                gPosMirror += 1

    return gPosMirror


"""Working!"""
x = solution([23, 10], [6, 4], [3, 2], 23)
assert x == 8, print(x)
x = solution([3, 2], [1, 1], [2, 1], 4)
assert x == 7, print(x)
x = solution([300, 275], [150, 150], [185, 100], 500)
assert x == 9, print(x)

"""Not Working :("""
# x = solution([2, 5], [1, 2], [1, 4], 11)
# assert x == 27, print(x)
# x = solution([10, 10], [4, 4], [3, 3], 5000)
# assert x == 739323, print(x)
