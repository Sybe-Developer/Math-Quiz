import random as r

def Lvl(v):
    if v==1:
        return r.randint(0,9)

    elif v==2:
        return r.randint(10,99)

    elif v==3:
        return r.randint(100,999)
    
def Game():
    s = 0

    print('\n')
    print('1 - 1 Digit \n2 - 2 Digit \n3 - 3 Digit')
    print('\n')
    v = int(input('Select The Level ->'))

    if v>3 or v==0:
        print('\n')
        print('Error')
        Game()
    else:
        pass

    for i in range(10):

        x = Lvl(v)
        y = Lvl(v)
        t = x+y

        print(f'{x} + {y}')
        ans = int(input('Enter the Answer ->'))
        
        if ans==t:
            print('Correct Answer')
            s+=1  
        else:
            print('Incorrect \nCorrect Answer is',t)

    print('\n')
    print('Your Score is ',s)
    print('Your Score(in %) is',s*10,'%')


print('Welcome to Math Quiz'.center(90))
print('\n')
print('Each Level contains 10 Ques')
print('Answer the following sums and Level shows no of digits')

while True:
    Game()
    print('\n')
    ch = input('Do you want to play game again? ->')
    if ch.upper() in ['Y','YES']:
        Game()
    else:
        break
        
    
