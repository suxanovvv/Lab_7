p=int(input('Введіть число p: '))
q=int(input('Введіть число q: '))
simple= 2, 3, 5, 7, 11, 13, 17, 19,\
        23, 29, 31, 37, 41, 43, 47,\
        53, 59, 61, 67, 71, 73, 79, \
        83, 89, 97, 101, 103, 107, \
        109, 113 , 127, 131,\
        137, 139, 149
for i in range(len(simple)):
    if p%simple[i]==0 and q%simple[i]==0:
        print('All q and p dividers: ', simple[i])
   
