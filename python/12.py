a=[0,1,2,3,4,5,6,7,8,9]
n = input('Ведіть послідовність: ')
n_list=n.split(' ')
for i in range(len(n)):
    if n[i] in a:
        spisok={a}-{n[i]}
        print(spisok)
    else:
        print('Error')
        
    
