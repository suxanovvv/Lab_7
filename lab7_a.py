#���� ��� p �� q. ������� �� ����� �� ������� ����� q, ������ ����� � p.
while True:
    while True:
        try:
            p=int(input('Input p = '))
            q=int(input('Input q = '))
            break
        except ValueError:
            print('Input numbers!! ')
        
    lst=[] #����� ������� �����
    for i in range(2, p+1): #��������� �� ��� ������ �� 2 �� p.
        for j in range(2, i): #��������� �� ����� �� 2 �� �����������.
            if i % j == 0: #���� ������ ���������, �� ����� �� ������.
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
