a = input('type your word: ')
count = 0
count1 = 0
count2 = 0
for son in a:
    if son.isdigit():
        count+=1
    elif son.isalpha():
        count1+=1
    else:
        count2+=1
print(f"words are: {count1} pcs \nnumbers are: {count} pcs \nsymbols are: {count2} pcs")
