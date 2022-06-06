from random import randint
s = int()
b = ''
komp = randint(1,10)
while b != 'yoq':
    print (komp)
    s = s + 1
    men = int(input("Son kiriting: "))
    if komp < men:
        natija = 'Kichikroq son kiriting.'
    elif komp > men:
        natija = 'Kattaroq son kiriting.'
    elif komp == men:
        natija = 'Yutdingiz!'
    print (natija)
    if natija == 'Yutdingiz!':
        b = input("O'yin tugadi davom ettirasizmi [ha/yoq] ? \n>>>:")
        s = int()
        komp = randint(1,10)
    if s == 5:
        s = int()
        komp = randint(1,10)
        b = input('Imkoniyatlar tugadi \nYana davom ettirasizmi? [ha/yoq] \n>>>: ')
if b == 'yoq':
    print ("O'yin tugadi. \nQatnashganingiz uchun rahmat")
