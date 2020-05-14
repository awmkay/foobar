from fractions import Fraction


def mMult(m1, m2):
    """Multiply two matrices: m1 * m2."""
    m1_row, m1_col = len(m1), len(m1[0])
    m2_row, m2_col = len(m2), len(m2[0])

    if m1_col != m2_row:
        raise ValueError('m1 columns must equal m2 rows')

    M = []
    for i in range(m1_row):
        M.append([])
        for j in range(m2_col):
            M[i].append([0])
            M[i][-1] = 0
            for k in range(m2_row):
                M[i][j] += m1[i][k] * m2[k][j]

    return M


def mSub(m1, m2):
    """Subract two matrices: m1 - m2."""
    rows, cols = len(m1), len(m1[0])
    return [[m1[i][j] - m2[i][j] for j in range(rows)] for i in range(cols)]


def eye(num):
    """Generate an Identity matrix of size num."""
    return [[int(x == y) for x in range(num)] for y in range(num)]


def mMinor(m, i, j):
    """Generate a copy of matrix m without row i or column j."""
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def mDet(m):
    """Compute the determinant of a matrix m."""

    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for col in range(len(m)):
        determinant += ((-1) ** col) * m[0][col] * mDet(mMinor(m, 0, col))
    return determinant


def mInv(m):
    """Generate the inverse of matrix m."""
    determinant = mDet(m)
    mLen = len(m)

    # special case for 2x2 matrix:
    if mLen == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for row in range(mLen):
        cofactorRow = []
        for col in range(mLen):
            minor = mMinor(m, row, col)
            cofactorRow.append(((-1) ** (row + col)) * mDet(minor))
        cofactors.append(cofactorRow)
    cofactors = mTran(cofactors)

    cLen = len(cofactors)
    for row in range(cLen):
        for col in range(cLen):
            cofactors[row][col] = cofactors[row][col] / determinant
    return cofactors


def mTran(m):
    """Generate the transpose of matrix m."""
    if type(m[0]) is not list:
        return [[m[i]] for i in range(len(m))]
    else:
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def lcm(nums):
    """Compute the lowest common multiple of a list of positive integers."""
    lcm = nums[0]
    for i in range(1, len(nums)):
        lcm = lcm * nums[i] // gcd(lcm, nums[i])
    return lcm


def gcd(a, b):
    """Compute the greatest common denominator of integers a and b."""
    while b:
        a, b = b, a % b
    return a


def solution(m):
    """Compute the steady state of an absorbing Markov matrix m."""
    steady = []
    nonSteady = []

    # Base case, saves compute time
    rows = len(m)
    if rows == 1:
        return [1, 1]

    # Store steady states etc.
    for i in range(rows):
        numZeros = m[i].count(0)
        if numZeros == rows:
            m[i][i] = 1
            steady.append(i)
        elif m[i][i] == 1 and numZeros == rows - 1:
            steady.append(i)
        else:
            nonSteady.append(i)

        rowSum = sum(m[i])
        for j in range(rows):
            m[i][j] = Fraction(m[i][j], rowSum)

    # If there is only steady states, stay in base state
    if not nonSteady:
        val = [0 for i in range(rows + 1)]
        val[0] = 1
        val[-1] = 1
        return val

    # if there is only one steady state it will end there
    steadyNum = len(steady)
    if steadyNum == 1:
        val = [0 for i in range(rows + 1)]
        val[steady[0]] = 1
        val[-1] = 1
        return val

    nonSteadyNum = len(nonSteady)

    # Calculate components of the transition matrix
    R = []
    for i in range(nonSteadyNum):
        R.append([])
        for j in range(steadyNum):
            R[i].append(m[nonSteady[i]][steady[j]])

    # Calculate components of the transition matrix
    Q = []
    for i in range(nonSteadyNum):
        Q.append([])
        for j in range(nonSteadyNum):
            Q[i].append(m[nonSteady[i]][nonSteady[j]])

    # Calculate the fundamental matrix
    F = mInv(mSub(eye(nonSteadyNum), Q))

    # Calculate the probability vector
    probVec = mMult(F, R)[0]

    # Modify values for output
    lowestMult = lcm([frac.denominator for frac in probVec])
    nums = [int(frac * lowestMult) for frac in probVec]
    nums.append(lowestMult)

    return nums


assert (
    solution([
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [4, 5, 5, 4, 2, 20]
)
