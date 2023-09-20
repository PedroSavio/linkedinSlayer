from PySimpleGUI import PySimpleGUI as sg
from linkdinSlayer import LinkdinSlayer

sg.theme('Reddit')

layout = [
    [sg.Text('Enter the linkdin email:'), sg.InputText(key='linkdin_email', size=(30, 1))],
    [sg.Text('Enter the linkdin password:'), sg.InputText(key='linkdin_password', password_char='*', size=(30, 1))],
    [sg.Text('Enter the job to search:'), sg.InputText(key='job_search', size=(30, 1))],
    [sg.Text('Enter the number of pages to search:'), sg.InputText(key='number_pages', size=(30, 1))],
    [sg.Text('Nivels:'), sg.DropDown(values=('Entry level', 'Internship', 'Junior level', 'Mid-Senior level', 'Director', 'Executive'), key='nivels', size=(30, 1))],
    [sg.Checkbox('Only easy apply', key='only_easy_apply')],
    [sg.Checkbox('Only remote', key='only_remote')],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

janela = sg.Window('Linkdin Slayer', layout)

while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        linkdin_email = values['linkdin_email']
        linkdin_password = values['linkdin_password']
        number_pages = values['number_pages']
        job_search = values['job_search']
        only_easy_apply = values['only_easy_apply']
        only_remote = values['only_remote']

        linkdin_slayer = LinkdinSlayer(linkdin_email, linkdin_password, number_pages, job_search, only_easy_apply, only_remote)
        linkdin_slayer.start_requests()

        print("Fim do programa")
        break
