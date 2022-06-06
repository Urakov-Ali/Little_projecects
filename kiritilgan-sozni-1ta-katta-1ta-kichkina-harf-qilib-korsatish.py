x =input('soz kiriting: ')
a = ''

for i in range(len(x)):
     if i%2==0:
          a += x[i].upper()
     else:
          a += x[i]
print (a)