from fractions import Fraction


def solution(dimensions, your_position, guard_position, distance):
    # Shorter Names
    xYou = your_position[0]
    yYou = your_position[1]

    maxBoxes = [int((distance + your_position[i]) / dimensions[i] + 1)
                for i in range(2)]

    # Counts number of possible hits
    gPosMirror = 0

    # Actually Used
    gFromR = dimensions[0] - guard_position[0]
    gFromL = guard_position[0]
    gFromT = dimensions[1] - guard_position[1]
    gFromB = guard_position[1]

    # Caclulate gradient from the guard to you.
    # Need the try due to possible ZeroDivisionError
    try:
        ygGrad = Fraction(gFromB - yYou, gFromL - xYou)
    except ZeroDivisionError:
        ygGrad = float("inf")

    # Save compute time
    distSqr = distance ** 2

    for x in range(-maxBoxes[0], maxBoxes[0]):
        for y in range(-maxBoxes[1], maxBoxes[1]):
            if x % 2:
                # Odd case
                xG = x * dimensions[0] + gFromR
            else:
                # Even case
                xG = x * dimensions[0] + gFromL

            if y % 2:
                # Odd case
                yG = y * dimensions[1] + gFromT
            else:
                # Even case
                yG = y * dimensions[1] + gFromB

            # If graident from mirrored guard and gradient from guard to you
            # are the same, then skip over (stops player shooting themself).
            # Need the try due to possible ZeroDivisionError
            try:
                if Fraction(yG - yYou, xG - xYou) == ygGrad:
                    continue
            except ZeroDivisionError:
                if ygGrad == float("inf"):
                    continue

            # Check whether the mirrored guard is within shooting distance.
            if (xG - xYou) ** 2 + (yG - yYou) ** 2 < distSqr:
                gPosMirror += 1

    return gPosMirror + 1


# """Working!"""
# x = solution([3, 2], [1, 1], [2, 1], 4)
# assert x == 7, print(x)
# x = solution([300, 275], [150, 150], [185, 100], 500)
# assert x == 9, print(x)

# """Not Working :("""
# x = solution([2, 5], [1, 2], [1, 4], 11)
# assert x == 27, print(x)
# x = solution([10, 10], [4, 4], [3, 3], 5000)
# assert x == 739323, print(x)
