c = "Kola narxi 1 donasi 5000 so'm"
a = int(input('Pulingiz qancha ?: '))
b = int(input(f'{c}\nNechta kola olasiz?: '))
d = 5000
e = b*d
f = a - e
if a>e:
    print (f"Qaytimingiz: {f}so'm \nHaridingiz uchun rahmat")
elif a<e:
    print (f"{-f} so'm pulingiz yetmayapti")
else:
    print ('Haridingiz uchun rahmat')

