def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def toFraction(a, b):
    denom = gcd(a, b)
    try:
        return (int(a / denom), int(b / denom))
    except ZeroDivisionError:
        return (float('inf'))


def solution(dimensions, your_position, guard_position, distance):
    # Shorter names for your position
    yFromL, yFromR = your_position[0], dimensions[0] - your_position[0]
    yFromB, yFromT = your_position[1], dimensions[1] - your_position[1]

    # Shorter names for guard position
    gFromL, gFromR = guard_position[0], dimensions[0] - guard_position[0]
    gFromB, gFromT = guard_position[1], dimensions[1] - guard_position[1]

    # Used for distance comparison
    distSqr = distance ** 2

    # Check if shooting the guard is possible
    if (gFromB - yFromB) ** 2 + (gFromL - yFromL) ** 2 > distSqr:
        return 0

    # Caclulate gradient from the base guard to you
    ygGrad = toFraction(gFromB - yFromB, gFromL - yFromL)

    # Stores all possible gradients from base to mirrored
    gGradSetTR, yGradSetTR = set(), set()
    gGradSetTL, yGradSetTL = set(), set()
    gGradSetBR, yGradSetBR = set(), set()
    gGradSetBL, yGradSetBL = set(), set()

    # Find number of necesary boxes
    maxBoxes = [distance // dimensions[i] + 1 for i in range(2)]

    # Loop through: 0 -> max, -1 -> min
    for x in list(range(-1, -maxBoxes[0], -1)) + list(range(maxBoxes[0])):
        # Decrease runtime by reducing computations
        xBox, xOdd, xPos = x * dimensions[0], x & 1, x >= 0

        # Caclulate mirrored x positions
        xY = xBox + yFromR if xOdd else xBox + yFromL
        xG = xBox + gFromR if xOdd else xBox + gFromL

        # Calculate mirrored x and base differences
        xgDiff, xyDiff = xG - yFromL, xY - yFromL

        for y in range(-maxBoxes[1], maxBoxes[1] + 1):
            # Decrease runtime by reducing computations
            yBox, yOdd, yPos = y * dimensions[1], y & 1, y >= 0

            # Calculate mirrored y positions
            yG = yBox + gFromT if yOdd else yBox + gFromB
            yY = yBox + yFromT if yOdd else yBox + yFromB

            # Calculate mirrored y and base differences
            ygDiff, yyDiff = yG - yFromB, yY - yFromB

            # Caclulate gradients from base you to mirrored you and guard
            gGrad = toFraction(ygDiff, xgDiff)
            yGrad = toFraction(yyDiff, xyDiff)

            # Skip iteration if distance to mirrored guard it too great
            if xgDiff ** 2 + ygDiff ** 2 > distSqr or gGrad == ygGrad:
                continue

            # Top Right
            if xPos and yPos:
                yGradSetTR.add(yGrad)
                if gGrad in yGradSetTR:
                    continue
                elif gGrad not in gGradSetTR:
                    gGradSetTR.add(gGrad)

            # Bottom Right
            elif xPos and not yPos:
                yGradSetBR.add(yGrad)
                if gGrad in yGradSetBR:
                    continue
                elif gGrad not in gGradSetBR:
                    gGradSetBR.add(gGrad)

            # Top Left
            elif not xPos and yPos:
                yGradSetTL.add(yGrad)
                if gGrad in yGradSetTL:
                    continue
                elif gGrad not in gGradSetTL:
                    gGradSetTL.add(gGrad)

            # Bottom Left
            else:
                yGradSetBL.add(yGrad)
                if gGrad in yGradSetBL:
                    continue
                elif gGrad not in gGradSetBL:
                    gGradSetBL.add(gGrad)

    # Add one for the straight shot
    shotNum = len(gGradSetTR) + len(gGradSetBR)
    shotNum += len(gGradSetTL) + len(gGradSetBL)
    return shotNum + 1


"""Working!"""
x = solution([3, 2], [1, 1], [2, 1], 4)
assert x == 7, print(x)
x = solution([2, 5], [1, 2], [1, 4], 11)
assert x == 27, print(x)
x = solution([300, 275], [150, 150], [185, 100], 500)
assert x == 9, print(x)
x = solution([23, 10], [6, 4], [3, 2], 23)
assert x == 8, print(x)
x = solution([3, 2], [1, 1], [2, 1], 1)
assert x == 1, print(x)


"""Not Working :("""
x = solution([10, 10], [4, 4], [3, 3], 5000)
assert x == 739323, print(x)
