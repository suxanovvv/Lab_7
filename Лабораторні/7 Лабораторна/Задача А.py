while True:
    while True:
        try:
            p=int(input('Input p = '))
            q=int(input('Input q = '))
            break
        except ValueError:
            print('Input numbers!! ')
        
    lst=[] #Пошук простих чисел
    for i in range(2, p+1): #Проходимо по всіх числах від 2 до p.
        for j in range(2, i): #Проходимо всі числа від 2 до теперішнього.
            if i % j == 0: #Якщо дільник знайдений, то число не просте.
                break
        else:
            lst.append(i)
    
    for k in range(len(lst)):
        if p%lst[k]==0 and q%lst[k]==0:
            print('All q and p dividers: ', lst[k])
    
    result=input('Input "1" to continue, and other to exit: ')
    if result=='1':
        continue
    break



