## Dice Game simulator
# Select a number between 1 and 6 and try to math with the Dice simulator

from random import randint


class DiceGame:
    def __init__(self):
        self.message='Select a integer number between 1 and 6: '

    def menu(self):             #method to initialize the game
        print('Dice Game Simulator'.center(60, '_'))
        print('x- to finish the game')
        n=input(self.message)
        return n

    def validation(self, n):  #validation if is an int number and if is between 1 and 6
        try:
            n = int(n)
            if  n >= 1 and n <=6 :
                return True
            else:
                print(f'{n} is not valid integer dice number. Only integer numbers between 1 and 6 are valid.')
                return False
        except:
            print(f'{n} is not an integer. Only integer numbers between 1 and 6 are valid.')


    def dice(self):             #Generate an integer random number between 1 and 6
        number=randint(1,6)
        return number

    def match(self,n,number):   #verify if the player number and the dice number match

        if int(n)==number:
            return f'Congratulations! You Won! \n Your number: {n} \n Dice number: {number}'
        else:
            return f'You Lose! \n Your number: {n}  \n Dice number: {number}'


d=DiceGame()
aux=0
while(aux!='x'):
    aux=d.menu()
    if d.validation(aux)==True:
        number=d.dice()
        print(d.match(aux,number))


