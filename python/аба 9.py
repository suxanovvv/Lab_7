n=10
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s_1 = {i for i in range(n)}
s_2 = {i for i in range(n)}
summa=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if(i in s_1) and (j in s_2):
            summa+=a[i][j]
            print(summa)
            
            
