while True:
    a_list=['Acer', 'HP', 'Lenovo', 'ASUS', 'Dell']
    b_list=['2200 Гц', '2300 Гц', '2400 Гц', '2500 Гц', '2600 Гц']
    c_list=['3 Гб', '4 Гб', '8 Гб', '16 Гб', '32 Гб']
    d_list=['17600', '22000', '24000', '26499', '32699']

    a={k:v for (k,v) in zip(a_list, b_list)}
    b={i:p for (i,p) in zip(a_list, d_list)}
    c={g:h for (g,h) in zip(a_list, c_list)}

    print('Назви усіх комп"ютерів: ', list(b.keys()))

    summa=int(b.pop('ASUS'))+int(b.pop('Acer'))+int(b.pop('HP'))+int(b.pop('Lenovo'))+int(b.pop('Dell'))
    arithmetic=summa/5
    print('Середня вартість: ', arithmetic)

    result=input('Input "1" to continue, and other to exit: ')
    if result=='1':
        continue
    break


