from random import randint
from PySimpleGUI import PySimpleGUI as sg

class DiceGame:

    def __init__(self):
    #create layout
    #theme
        sg.theme('Reddit')

        layout = [
            [sg.Text('Select an integer number between 1 and 6'), sg.Input(key='number')],  # line1
            [sg.Button('Generate')],  # line2
            [sg.Output(size=(80,10))],
        ]

        #create window
        self.w1=sg.Window('Dice Game Simulator').layout(layout)

    def menu(self):  # method to initialize the game
        # obtain value
        self.event, self.value = self.w1.read()
        # convert dict to str
        val = self.value.get('number')

        return self.event, val


    def dice(self):             #Generate an integer random number between 1 and 6
        number=randint(1,6)
        return number

    def match(self,n,number):   #verify if the player number and the dice number match
        if int(n)==number:
            return f'Congratulations! You Won! \n Your number: {n} \n Dice number: {number}'
        else:
            return f'You Lose! \n Your number: {n}  \n Dice number: {number}'

    def validation(self, n):  #validation if is an int number and if is between 1 and 6
        try:
            n = int(n)
            if  n >= 1 and n <=6:
                return True
            else:
                print(f'{n} is not valid integer dice number. Only integer numbers between 1 and 6 are valid.')
                return False
        except:
                print(f'{n} is not an integer. Only integer numbers between 1 and 6 are valid.')
                return False



d=DiceGame()

while True:
    event, val=d.menu()

    #when window close, stop program
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Generate':
        status=d.validation(val)
        if status==True:
            number=d.dice()
            print(d.match(int(val),number))




