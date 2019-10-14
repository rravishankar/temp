# python3

EPS = 1e-6
PRECISION = 20



def readEquation():
    size = int(input())
    a = []
    # print("Size", size)
    for row in range(size):
        line = list(map(float, input().split()))
        # print("Line", line)
        a.append(line)
        # print("a:", a)
    return a




def swap_row(mat, i, j):
    temp = mat[i]
    mat[i] = mat[j]
    mat[j] = temp
    return mat


def forwardElim(mat):
    for k in range(len(mat)):
        # initialize maximum value for and index for pivot
        i_max = k
        v_max = mat[i_max][k]

        # find greater amplitude for pivot if any
        for i in range(k+1, len(mat)):
            if mat[i][k] > v_max:
                i_max = i
                v_max = mat[i][k]
        if mat[i_max][k] == 0:
            return k

        if i_max != k:
            mat = swap_row(mat, k, i_max)

        for i in range(k+1, len(mat)):
            f = mat[i][k]/mat[k][k]

            for j in range(k+1, len(mat) + 1):
                mat[i][j] -= mat[k][j] * f
            mat[i][k] = 0
    #     print("Mat (inner loop for k={}) is {}".format(k, mat))
    # print("Mat (end of outer loop) is ", mat)
    return -1, mat


def backSub(mat):
    N = len(mat)
    x = [0] * N
    # print("backSub: mat is {}".format(mat))

    for i in range(N-1, -1, -1):
        # print("Got i: {} N:{}".format(i,N))
        x[i] = mat[i][N]  # RHS
        for j in range(i+1, N):
            # print("x[i] = x[{}] = {}  x[j] = x[{}] = {} mat[i][j]: mat[{}][{}]= {}".format(i, x[i], j, x[j], i,j, mat[i][j]))
            x[i] -= mat[i][j]*x[j]
        # print("Setting x[i]= x[{}] to x[i]/mat[i][i]= x[{}]/mat[{}][{}] = {}/{}= {}".format(i,i,i,i,x[i], mat[i][i],x[i]/mat[i][i] ))
        x[i] = x[i]/mat[i][i]
        
    # print("Solution for the system is")
    for i in range(N):
        print(x[i], end=" ")


def gaussianElimination(mat):
    singular_flag, mat = forwardElim(mat)

    if singular_flag != -1:
        print("Singular matrix")
        if mat[singular_flag][len(mat)]:
            print("Inconsistent system")
        else:
            print("May have infinitely many solutions")
        return
    backSub(mat)


if __name__ == "__main__":
    equation = readEquation()
    # equation = [[3.0, 2.0, -4.0, 3.0], [2.0, 3.0, 3.0, 15.0], [5.0, -3, 1.0, 14.0]]

    # print(equation)
    gaussianElimination(equation)

    exit(0)
