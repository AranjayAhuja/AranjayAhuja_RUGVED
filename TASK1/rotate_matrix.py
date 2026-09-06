def rotate_matrix(mat, order):
    for row in range(order):
        for col in range(row + 1,order):
            temp = mat[row][col]
            mat[row][col] = mat[col][row]
            mat[col][row] = temp
    for row in range(order):
        mat[row].reverse()


def spiral(mat, order):
    top_wall = 0
    bottom_wall = order - 1
    left_wall = 0
    right_wall = order -1
    print("Spiral order: ", end="")
    while top_wall<= bottom_wall and left_wall<= right_wall:
        for col in range(left_wall, right_wall+1):
            print(mat[top_wall][col],end=" ")
        top_wall += 1
        for row in range(top_wall, bottom_wall+1):
            print(mat[row][right_wall],end=" ")
        right_wall -= 1
        if top_wall <= bottom_wall:
            for col in range(right_wall, left_wall-1,-1):
                print(mat[bottom_wall][col],end=" ")
            bottom_wall -= 1
        if left_wall <= right_wall:
            for row in range(bottom_wall, top_wall-1, -1):
                print(mat[row][left_wall],end=" ")
            left_wall += 1
    print()


n = int(input("Order of matrix: "))
mat = []
print("Enter elements for each row seperated by spaces")
for i in range(n):
    r_elm = input(f"Row {i+1}: ")
    r_list = r_elm.split()
    Row = []
    for j in r_list:
        Row.append(int(j))
    mat.append(Row)

print("Original matrix:  ")
for row in mat:
    print(row)
rotate_matrix(mat, n)
print("Rotated matrix:  ")
for row in mat:
    print(row)
spiral(mat, n)
