import PySimpleGUI as sg
import pyttsx3

text_speech = pyttsx3.init()
voice_answer = text_speech.getProperty('voices')


layout = [    [sg.Text('Choose voice:',text_color='blue',background_color='black'),sg.Radio('Male', 'RADIO1', default=True, key='male_voice',background_color='chocolate'),sg.Radio('Female', 'RADIO1', key='female_voice',background_color='purple')],
     [sg.Text('Enter text here:',text_color='black',background_color='pink',)],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='gray')],
   
    
]

window = sg.Window('Caleb Text Reader', layout,background_color='navy blue')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['male_voice']:
            text_speech.setProperty('voice', voice_answer[0].id)
        elif values['female_voice']:
           text_speech.setProperty('voice', voice_answer[1].id) 
    
        text_speech.say(text)
        text_speech.runAndWait()

window.close()