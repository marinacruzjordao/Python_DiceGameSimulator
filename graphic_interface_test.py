from PySimpleGUI import PySimpleGUI as sg

class Teste:

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
        # print('Dice Game Simulator'.center(60, '_'))
        # print('x- to finish the game')

        # obtain value
        self.event, self.value = self.w1.read()

        # convert dict to str
        val = self.value.get('number')

        return self.event, val

t=Teste()
#read events
while True:
    #unpacking
    #event,value=w1.read()
    event, val=t.menu()
    #when window close, stop program
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Generate':
        print('You Won')



