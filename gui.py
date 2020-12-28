from detector import Detector
import PySimpleGUI as gui

# detector = Detector('yolo_support_files', size=(320,320)) #Create a detector 

layout = [
    [gui.Text('YOLO Video Player', size=(22,1), font=('Any',18,'Bold'),text_color='#1c86ee' ,justification='left'),]
    ]

# Layout of the popup window
layout1 = [[gui.Image(filename='', key='videoOut',tooltip='Video goes here.', size=(320,320))],
          [gui.ReadButton(button_text='Play',key='playbtn'), gui.Exit()]]

# Initialize window
window = gui.Window('Object detector')
window.Layout(layout).finalize()



while True:
    event, values = window.Read(timeout=0)
    if event == gui.WIN_CLOSED or event == 'Exit':
        break

    
window.close()