
# Strassen's Matrix Multiplication Algorithm

def add_matrix(A, B):
    n = len(A)

    return [
        [A[i][j] + B[i][j] for j in range(n)]
        for i in range(n)
    ]


def subtract_matrix(A, B):
    n = len(A)

    return [
        [A[i][j] - B[i][j] for j in range(n)]
        for i in range(n)
    ]


def strassen(A, B):

    n = len(A)

    # Base condition
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide matrix A
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide matrix B
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Calculate seven products
    M1 = strassen(
        add_matrix(A11, A22),
        add_matrix(B11, B22)
    )

    M2 = strassen(
        add_matrix(A21, A22),
        B11
    )

    M3 = strassen(
        A11,
        subtract_matrix(B12, B22)
    )

    M4 = strassen(
        A22,
        subtract_matrix(B21, B11)
    )

    M5 = strassen(
        add_matrix(A11, A12),
        B22
    )

    M6 = strassen(
        subtract_matrix(A21, A11),
        add_matrix(B11, B12)
    )

    M7 = strassen(
        subtract_matrix(A12, A22),
        add_matrix(B21, B22)
    )

    # Calculate four result submatrices
    C11 = add_matrix(
        subtract_matrix(add_matrix(M1, M4), M5),
        M7
    )

    C12 = add_matrix(M3, M5)

    C21 = add_matrix(M2, M4)

    C22 = add_matrix(
        add_matrix(subtract_matrix(M1, M2), M3),
        M6
    )

    # Combine result matrices
    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


def next_power_of_two(n):
    return 1 << (n - 1).bit_length()


def matrix_multiplication(A, B):

    rows = len(A)
    cols = len(B[0])
    inner = len(B)

    if inner != len(A[0]):
        raise ValueError("Incompatible matrix dimensions")

    # Pad matrices to a square power-of-two size
    size = next_power_of_two(max(rows, inner, cols))

    A_pad = [
        [0] * size for _ in range(size)
    ]

    B_pad = [
        [0] * size for _ in range(size)
    ]

    for i in range(rows):
        for j in range(inner):
            A_pad[i][j] = A[i][j]

    for i in range(inner):
        for j in range(cols):
            B_pad[i][j] = B[i][j]

    C_pad = strassen(A_pad, B_pad)

    # Remove padding
    return [
        C_pad[i][:cols] for i in range(rows)
    ]


# Main program
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication is not possible.")

else:

    print("Enter first matrix elements:")
    A = [
        list(map(int, input().split()))
        for _ in range(r1)
    ]

    print("Enter second matrix elements:")
    B = [
        list(map(int, input().split()))
        for _ in range(r2)
    ]

    result = matrix_multiplication(A, B)

    print("\nResultant Matrix:")

    for row in result:
        print(row)
