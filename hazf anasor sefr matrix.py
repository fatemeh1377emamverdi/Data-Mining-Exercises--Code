Rows = int(input("Enter the number of rows:"))
Columns = int(input("Enter the number of columns:"))
matrix = []
for i in range(Rows):
    a =[]
    for j in range(Columns):
        a.append(int(input()))
    matrix.append(a)
for i in range(Rows):
    for j in range(Columns):
        if matrix[i][j] !=0:
            print(matrix[i][j], end = " ")
    print()