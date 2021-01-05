def print_matrix(mat: dict):
    result = []
    for a in mat.keys():
        b = mat[a]
        for b in mat[a].keys():
            c = mat[a][b]
            print("(", a, ", ", b, ", ", c, ")")
            result.append((a, b, c))
    return result
def input_matrix(n, m):
    vector = dict()
    for a in range(n):
        for b in range(m):
            c = int(input("(" + str(a) + ',' + str(b) + '): '))
            if c != 0:
                if a not in vector:
                    adict = dict()
                else:
                    adict = vector[a]
                adict[c] = c
                vector[a] = adict
    return vector
def transpose(mat):
    result = dict()
    for a in mat.keys():
        b = mat[r]
        for b in mat[a].keys():
            if b not in result:
                rdict = dict()
            else:
                adict = result[b]
            adict[a] = mat[a][b]
            result[b] = adict
    return result
def add(mat1, mat2):
    ans = mat1;
    for a in mat2.keys():
        b = mat2[a]
        for b in mat2[a].keys():
            if a in ans:
                if b in ans[a]:
                    ans[a][b] += mat2[a][b]
                else:
                    ans[a][b] = mat2[a][b]
            else:
                ans[a][b] = mat2[a][b]
    return ans;
def get_element(mat, i, j):
    if i not in mat:
        return 0
    if j not in mat[i]:
        return 0
    return mat[i][j]
def multiple(mat1, mat2, n, m, z):
    result = dict()
    for i in range(n):
        for j in range(z):
            for k in range(m):
                val = get_element(mat1, i, k) * get_element(mat2, k, j)
                c = get_element(result, i, j) + val
                if i in result:
                    adict = result[i]
                else:
                    adict = dict()
                adict[j] = c
                result[i] = adict
    return result
n = int(input("enter number of rows first matrix: "))
m = int(input("enter number of columns first matrix: "))
print("number of rows second matrix ", m)
z = int(input("enter number of columns second matrix: "))
print("First Matrix")
mat1 = input_matrix(n, m)
print("Second Matrix")
mat2 = input_matrix(m, z)
nmat = multiple(mat1, mat2, n, m , z)
print_matrix(nmat)