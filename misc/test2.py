import PySimpleGUI as sg

layout = [
    [sg.Text('Location'), sg.InputText()],
    [sg.FileBrowse('Browse'), sg.Button('Submit')],
    [sg.Text((''), key='file')]
]

window = sg.Window("Hack the Job", layout, element_justification='c').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == 'Browse':
        file = values[]
        window['file'].update(file
    if event == 'Submit':
        sg.popup('hi')

window.close()
