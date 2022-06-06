a = input ("Iltimos tarifni tanlang \n>>> Sutka/Soat: ")
if a == str('soat'):
   a = 30000
if a == str('sutka'):
   a = 120000
b = int(input("Necha sutkaga/soatga qolmoqchisiz: "))
c = b*a
d = input("Tarifni kiriting \n>>> [ekonom]/[komfort]/[biznes]: ")
if d == str('ekonom'):
   e = c
if d == str('komfort'):
    if a == 30000:
       e = (c+10000)
    elif a == 120000:
         e = (c+50000)
if d == str('biznes'):
    if a == 30000:
       e = (c+25000)
    elif a == 120000:
         e = (c+80000)
if e>200000:
    r = int(e/10)
    t = int(e - r)
    print (f"Sizning umumiy tarifingiz \nnarxi:{e} so'm \nChegirma miqdori:{r} so'm \nTarifingiz narxi\n(chegirma bilan): {t} so'm")
elif e>100000:
    r = int(e/20)
    t = int(e - r)
    print (f"Sizning umumiy tarifingiz \nnarxi:{e} so'm \nChegirma miqdori:{r} so'm \nTarifingiz narxi\n(chegirma bilan): {t} so'm")
    
    
