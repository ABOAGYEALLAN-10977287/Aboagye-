import PySimpleGUI as psg
import qrcode

layout=[  
     [psg.Input(key='char_input')],
     [psg.Button('Generate',key='start_Button')],
     [psg.Image('',key='image_key')]
]





window=psg.Window('qrcode Generator', layout)

while True:
    event, values = window.read()
    if event==psg.WIN_CLOSED:
        break

    if event == 'start_Button':
        input=values['char_input']
        image = qrcode.make(input)
        image.save('qr.png')
        window['image_key'].update('qr.png')
     
















