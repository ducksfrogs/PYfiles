import PySimpleGUI as sg
sg.theme('DarkAmber')

layout = [  [sg.Text("Some text on Row1")],
            [sg.Text("TITLE"), sg.InputText()],
            [sg.Text("PRICE"), sg.InputText()],
            [sg.Text("mmo"), sg.InputText()],
            [sg.Button('INSERT'), sg.Button("VIEW")],  
            [sg.Button('OK'), sg.Button("Cancel")]  ]

window = sg.Window("Window Title", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print("You entered ", values[0])

window.close()
