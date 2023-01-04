#matrix multiplication,trace,commutative check
X= [[1,2],
      [4,5]]
      
Y = [[2,2],
       [4,5]]
print("X=")
for x in X:
	print(x)
print("Y=")
for y in Y:
	print(y)	
result1 = [[0,0],
               [0,0]]           
result2 = [[0,0],
                [0,0]]
for i in range(len(X)):
   
   for j in range(len(Y[0])):
       
       for k in range(len(Y)):
  
               result1[i][j] += X[i][k] * Y[k][j]
print("multiplication of XY=")
for r1 in result1:
      print(r1)
for i in range(len(Y)):
   
   for j in range(len(X[0])):
       
       for k in range(len(X)):
                     result2[i][j] += Y[i][k] * X[k][j]
print("multiplication of  YX=")
for r2 in result2:
	print(r2)
Tr1=0
Tr2=0
for i in range(2):
	Tr1=Tr1+result1[i][i]
	Tr2=Tr2+result2[i][i]
print("trace of XY=",Tr1)
print("trace of YX=",Tr2)
if Tr1==Tr2:
	print("Therefore trace XY= trace YX")
sub=[[0,0],
         [0,0]]
for i in range(len(X)):
	for j in range(len(Y)):
		sub[i][j]=result1[i][j]-result2[i][j]
print("XY-YX=")
for s in sub:
	print(s)
if sub!=[[0,0],[0,0]]:
                 print("X and Y are not commutative")