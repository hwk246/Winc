import PySimpleGUI as sg


def create_window(data, message='Message'):

    information = data

    layout = [[information], [sg.Button('Ok')]]

    window = sg.Window(message, layout, element_justification='c')

    while True:
            event, values = window.read()
            if event == 'Ok' or event == sg.WIN_CLOSED:
                break

    window.close