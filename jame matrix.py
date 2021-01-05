def a_matrix(mat: dict):
    result = []
    for a in mat.keys():
        b = mat[a]
        for b in mat[a].keys():
            c = mat[a][b]
            print("(", a, ", ", b, ", ", c, ")")
            result.append((a, b, c))
    return result
def b_matrix():
    n = int(input("enter number of rows: "))
    m = int(input("enter number of columns: "))
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
        b = mat[a]
        for b in mat[a].keys():
            if b not in result:
                adict = dict()
            else:
                adict = result[b]
            adict[a] = mat[a][b]
            result[b] = adict
    return result
def add(mat1 , mat2):
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
mat1 = b_matrix()
mat2 = b_matrix()
nmatrix = add(mat1, mat2)
a_matrix(nmatrix)