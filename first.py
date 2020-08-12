n=int(input("Enter number of rows "))
m=int(input("Enter number of columns "))
mat=[]
print("Enter elements :")
for i in range(0,n):
    arr=[]
    for j in range(0,m):
        z=int(input())
        arr.append(z)
    mat.append(arr)

for i in range(0,n):
    for j in range(0,m):     
        print(mat[i][j],end=" ")
    print()

    
    