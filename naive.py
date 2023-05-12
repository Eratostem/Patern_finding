f = open('Horla.txt').read()
#f = str('ababababaaaabb')
print(type(f))
patern = input("Patern to look for : ")
clock = 0
for letter in f:
    pattern_test = str('')
    letter_nb = 0
    while letter_nb < len(patern) and f[clock+letter_nb]==patern[letter_nb]:
        pattern_test = pattern_test + str(f[clock+letter_nb])
        letter_nb += 1
        
    if patern == pattern_test:
        print("patern found at caracter "+ str(clock))
    clock += 1
