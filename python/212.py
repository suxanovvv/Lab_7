days = range (1, 32)
mounths = range (1, 13)
years = range (1901, 2020)
d, m, y = int (input ( 'day: ')), int(input('mounth: ')), int(input('year: '))
if mounths==4 or mounths==6 or mounths==9 or mounths==11:
    print('Previous Data: ', days-1,'.', mounth,'.', year, 'Next Day: ', '1.', mounth+1, year)
    
        
    
