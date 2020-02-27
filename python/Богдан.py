#15 Опанасюк
N=(input('Введіть послідовність: '))
u_list=list(map(int,N.split()))
a_list=[]
b_list=[]
for i in range(len(u_list)):
    if u_list[i]%2==0:
        a_list.append(u_list[i])
    else:
        b_list.append(u_list[i])
print("parni:")
for n in a_list:
    print(n,end=' ')
print()
print("neparni")
for n in b_list:
    print(n,end=' ')
print()

    
            
