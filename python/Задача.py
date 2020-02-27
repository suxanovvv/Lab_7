#3 Суханов
N=(input('Введіть послідовність чисел: '))
g_list=N.split()
counter=0
for i in range(len(g_list)):
    if g_list[i]=='0':
        counter+=1
print('Кількість нулів у послідовності: ', counter)
        
    
    
