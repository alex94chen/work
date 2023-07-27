x = input('Guess a letter: ').lower()
if(len(x) > 1 and not x.isalpha()):
    print('E3')

elif(len(x) > 1):
    print('E1')
    
elif(not x.isalpha()):
    print('E2')
     
else:
    print(x)
