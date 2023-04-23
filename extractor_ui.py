import PySimpleGUI as sg
from extractor import open_file_and_extract

TITLE = "Even And Odd Extractor"

sg.theme('GrayGrayGray')

window = sg.Window(TITLE)

layout = [
    [sg.Text('', size=(20,1)), sg.Text(TITLE, font=('Any 20'), auto_size_text=True, justification='center'), sg.Text('', size=(20,1))],
    [sg.Text('File name to open: ')],
    [sg.Input(), sg.FileBrowse()],
    [sg.Button('Upload'), sg.Button('Quit')]
]

window.layout(layout)

while True:
    event, values = window.read()

    if(event == sg.WIN_CLOSED or event == 'Quit'):
        break

    if(event == 'Upload'):
        open_file_and_extract(values[0])
        sg.popup_quick_message('New files successfully created within this directory')

window.close()