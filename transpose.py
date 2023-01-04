a=[[1,2],
    [7,6]]
x=[[0,0],
     [0,0]]
print("A=")
for aa in a:
	print(aa)
for i in range(len(a)):
	for j in range(len(a)):
		x[i][j]=a[j][i]
print("Atranspose=")
for aT in x:
	print(aT)