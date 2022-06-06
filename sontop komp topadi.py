from random import randint
s = 0
while True:
    a = randint(1,10)
    s = s + 1
    d = input(f"{a} sonini o'yladinigzmi? >>>: ")
    if d == 'ha':
        break
print (f"kompyuter {s} martta urinishda topdi.")
    
