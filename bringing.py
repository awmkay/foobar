from fractions import Fraction


def solution(dimensions, your_position, guard_position, distance):
    maxBoxes = [int((distance / dimensions[i] / 2) + 1) for i in range(2)]
    gPosMirror = []

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

            gDist = (xG - yFromL) ** 2 + (yG - yFromB) ** 2
            if gDist < distance ** 2:
                gPosMirror.append((xG, yG))

    return len(gPosMirror)


# print(solution([3, 3], [1, 1], [2, 2], 8))
# print(solution([3, 2], [1, 1], [2, 1], 4))
# print(solution([300, 275], [150, 150], [185, 100], 500))
