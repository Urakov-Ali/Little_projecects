soz = 'salom python assalom python salom dunyo'
word = soz.split()
a = []
for i in word:
    s = word.count(i)
    f = f'{i} {s} ta'
    if f not in a:
        a.append(f)
for i in a:
    print (i)




