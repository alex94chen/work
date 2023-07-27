stons = int(input('Enter three digits (each digit for one pig): '))


pig_1 = int(stons / 100)
pig_2 = int(stons / 10) % 10
pig_3 = int(stons % 10)

all_stons = pig_1 + pig_2 + pig_3
division = int(all_stons / 3)
rest_division = all_stons % 3
boo_division = bool(not(stons % 3))
    
print(all_stons, division, rest_division, boo_division)
