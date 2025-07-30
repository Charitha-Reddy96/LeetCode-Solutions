n = 5 
mat = [[" " for j in range(n)] for i in range(n)]
print(mat)        
       
for i in range(n):
    for j in range(i, n):
        if i == j:
            mat[i][j] = "*"
j = n-1          
for i in range(n):
    mat[i][j-i] = "*"

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()   