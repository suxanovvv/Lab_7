#p=int(input('p '))
#q=int(input('q '))
f=int(input('The most simple digit: '))
a={i for i in range(2,f+1) if f%f==0 and f%2==0}
print(a)
