def gcd(a, b):
    """Compute the greatest common denominator of integers a and b."""
    return a if b == 0 else gcd(b, a % b)


def toGradient(pt1, pt2):
    """Convert pt1 and pt2 to simplified gradient (numerator, denominator)."""
    xDiff = pt1[0] - pt2[0]
    yDiff = pt1[1] - pt2[1]
    denom = gcd(yDiff, xDiff)

    if not xDiff:
        return float("inf")
    elif not yDiff:
        return 0
    else:
        return (yDiff // denom, xDiff // denom)


def solution(dim, mPos, gPos, dist):
    # Used for distance calculations
    distSqr = dist ** 2

    # Check you can shoot the guard
    if (gPos[0] - mPos[0]) ** 2 + (gPos[1] - mPos[1]) ** 2 > distSqr:
        return 0

    # Max number of boxes to be mirrored
    maxBox = [dist // dim[0] + 2, dist // dim[1] + 2]

    # Used for
    baseGrad = toGradient(mPos, gPos)

    xRange = list(range(maxBox[0])) + list(range(-1, -maxBox[0], -1))
    yRange = list(range(maxBox[1])) + list(range(-1, -maxBox[1], -1))

    # Store gradients from base me to mirrored me and guards
    gGradSet = set()
    mGradSet = set()

    # Stores number of positive x shots that hit a guard first
    posShots = 0

    for x in xRange:
        # Reset sets for negative x values in case of parallel gradients
        if x == -1:
            posShots += len(gGradSet)
            mGradSet.clear()
            gGradSet.clear()

        # Used for later calculations
        xOdd = x & 1
        xBox = x * dim[0]

        # Calculate mirrored x positions of me and guard
        xG = xBox + dim[0] - gPos[0] if xOdd else xBox + gPos[0]
        xM = xBox + dim[0] - mPos[0] if xOdd else xBox + mPos[0]

        # Used for distance checking
        xGSqr = (xG - mPos[0]) ** 2
        for y in yRange:
            # Used for later calculations
            yOdd = y & 1
            yBox = y * dim[1]

            # Calculate mirrored y positions of me and guard
            yG = yBox + dim[1] - gPos[1] if yOdd else yBox + gPos[1]
            yM = yBox + dim[1] - mPos[1] if yOdd else yBox + mPos[1]

            # Used for distance checking
            yGSqr = (yG - mPos[1]) ** 2

            # Check for xG within ray distance
            if xGSqr + yGSqr > distSqr:
                continue

            # Calculate gradients from base me to mirrored me and guard
            mGrad = toGradient((xM, yM), mPos)
            gGrad = toGradient((xG, yG), mPos)

            # Skip if mirrored guard is in line with base me and guard
            if gGrad == baseGrad:
                continue

            # Add new mGradient for parallel checking
            if mGrad not in mGradSet:
                mGradSet.add(mGrad)

            # Add gGradient if if does not have another guard or me in it's way
            if gGrad not in gGradSet and gGrad not in mGradSet:
                gGradSet.add(gGrad)

    return posShots + len(gGradSet) + 1


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

"""Not Working: ("""
x = solution([10, 10], [4, 4], [3, 3], 5000)
assert x == 739323, print(x)
