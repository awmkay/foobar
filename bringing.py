from fractions import Fraction


def solution(dimensions, your_position, guard_position, distance):
    # Shorter names for your position
    xYou, yYou = your_position[0], your_position[1]

    # Shorter names for guard position
    gFromR = dimensions[0] - guard_position[0]
    gFromL = guard_position[0]
    gFromT = dimensions[1] - guard_position[1]
    gFromB = guard_position[1]

    # Used for distance comparison
    distSqr = distance ** 2

    # Find number of necesary boxes
    maxBoxes = [int((distance + your_position[i]) / dimensions[i])
                for i in range(2)]

    # Stores all possible gradients that lead to hits
    gGradList = []

    # Used multiple times for gradient comparison
    inf = float("inf")

    # Caclulate gradient from the base guard to you
    try:
        ygGrad = Fraction((gFromB - yYou), (gFromL - xYou))
    except ZeroDivisionError:
        ygGrad = inf

    for x in range(-maxBoxes[0], maxBoxes[0] + 1):
        # Decrease runtime by reducing computations
        xBox = x * dimensions[0]
        xOdd = x % 2
        for y in range(-maxBoxes[1], maxBoxes[1] + 1):
            # Decrease runtime by reducing computations
            yBox = y * dimensions[1]
            yOdd = y % 2

            # Calculate mirrored guard position
            xG = xBox + gFromR if xOdd else xBox + gFromL
            yG = yBox + gFromT if yOdd else yBox + gFromB

            # Decrease runtime by reducing computations
            xgDiff, ygDiff = xG - xYou, yG - yYou

            # If graident from mirrored guard and gradient from guard to you
            # are the same, then skip over (stops player shooting themself).
            # Need the try due to possible ZeroDivisionError
            try:
                grad = [Fraction(ygDiff, xgDiff)]
                if grad[0] == ygGrad:
                    continue
            except ZeroDivisionError:
                grad[0] = inf
                if grad[0] == ygGrad:
                    continue

            # Adding bool to ensure gradients for points in opposite directions
            # don't cancel eachother out
            if grad[0] >= 0 and grad[0] != inf:
                grad.append(xG > xYou)
            else:
                grad.append(yG > yYou)

            # Check whether the mirrored guard is within shooting distance
            # and whether the shot has already been fired
            if xgDiff ** 2 + ygDiff ** 2 < distSqr \
                    and grad not in gGradList:
                gGradList.append(grad)

    # Add one for the straight shot
    return len(gGradList) + 1


"""Working!"""
# x = solution([300, 275], [150, 150], [185, 100], 500)
# assert x == 9, print(x)
# x = solution([3, 2], [1, 1], [2, 1], 4)
# assert x == 7, print(x)
x = solution([2, 5], [1, 2], [1, 4], 11)
assert x == 27, print(x)


"""Not Working :("""
# x = solution([10, 10], [4, 4], [3, 3], 5000)
# assert x == 739323, print(x)
