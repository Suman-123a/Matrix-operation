def trans(a):
	x=[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(len(a)):
		for j in range(len(a)):
			x[i][j]=a[j][i]
	return x
def m(X,Y):
	result1=[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(len(X)):
   
         for j in range(len(Y[0])):
       
               for k in range(len(Y)):
               	result1[i][j] += X[i][k] * Y[k][j]
	return result1
A=[[3,2,-1],[0,3,2],[1,-3,4]]
B=[[2,-2,3],[1,1,0],[3,2,1]]
At=trans(A)
Bt=trans(B)
print("The transpose of A")
for i in At:
	print(i)
print("The transpose of B")
for i in Bt:
	print(i)
AB=m(A,B)
ABt=trans(AB)
AtBt=m(Bt,At)
print("The result of (AB)T")
for i in ABt:
	print(i)
print("The result of (BT)(AT)")
for i in AtBt:
	print(i)