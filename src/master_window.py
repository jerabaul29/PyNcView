import PySimpleGUI as sg

sg.theme('DarkBlue14')

layout = [[sg.Text('File', size=(4, 1)), sg.Input(key="-FILE-", default_text=".nc file", size=(128, 2)), sg.FileBrowse()],
          [sg.Button("Select file", key="-SELECT_FILE-"), sg.Button("Cancel", key="-SELECT_CANCEL-"), sg.Button("Show attributes", key="-SHOW_ATTRIBUTES-")]]

window = sg.Window('PyNcView - v0.0', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
