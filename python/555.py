a=int(input('kilkist kvartir'))
n=int(input('otchet'))
count=0
if a<n:
    for i in range(n,a+1):
        count+=i
elif a>n:
    for i in range(a,n+1):
        count+=i
if count%2==0:
    print('true')
else:
    print('false')
    
