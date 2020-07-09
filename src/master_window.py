import PySimpleGUI as sg
import netCDF4 as nc4
import pprint

pp = pprint.PrettyPrinter(indent=4)

sg.theme('DarkBlue14')

file_select_prompt = ".nc file or OpenDAP url"

layout = [[sg.Text('File', size=(4, 1)), sg.Input(key="-FILE-", default_text=file_select_prompt, size=(128, 2)), sg.FileBrowse()],
          [sg.Button("Select file", key="-SELECT_FILE-"), sg.Button("Cancel", key="-SELECT_CANCEL-"), sg.Button("Show attributes", key="-SHOW_ATTRIBUTES-")]]

main_window = sg.Window('PyNcView - v0.0', layout)

selected_file = None
active_show_attributes = False
ignore_main_close = False

while True:
    event, values = main_window.read(timeout=100)
    # print(event, values)

    if event == "-SELECT_FILE-":
        try:
            selected_file = values["-FILE-"]
            nc_dataset = nc4.Dataset(selected_file)
        except:
            selected_file = None
            sg.Popup('Unable to open .nc file or OpenDAP url!')

    if event == "-SELECT_CANCEL-":
        selected_file = None
        main_window.FindElement("-FILE-").Update(file_select_prompt)
        # TODO: reset also the path in the browser

    if event == "-SHOW_ATTRIBUTES-":
        if selected_file is None:
            sg.Popup('Select file first!')
        else:
            active_show_attributes = True

            # TODO: make more beautiful / filter
            attributes_doc = pp.pformat(nc_dataset.variables)
            attributes_doc = attributes_doc.replace('\x00','')
            type(attributes_doc)
            print(attributes_doc)

            layout = [[sg.Multiline(attributes_doc, size=(128, 64))]]

            attributes_window = sg.Window('Data attributes', layout)

    if active_show_attributes:
        event, values = attributes_window.read(timeout=100)

        if event == sg.WIN_CLOSED:
            attributes_window.close()
            ignore_main_close = True
            active_show_attributes = False

    if event == sg.WIN_CLOSED:
        if not ignore_main_close:
            break
        ignore_main_close = False
