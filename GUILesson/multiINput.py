import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text("Persistent window")],
          [sg.Input('-IN')],
          [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window tha stays open', layout)

while True:
    evant, values = window.read()
    print(evant, values)
    if evant == sg.WIN_CLOSED or evant == 'Exit':
        break
window.close()
