from detector import Detector
import PySimpleGUI as gui
import Detector as det


# Create a detector
detector = Detector('yolo_support_files', size=(320,320))

# Define layout
layout = [[gui.Image(filename='', key='videoOut',tooltip='Video goes here.', size=(480,320))],
          [gui.ReadButton(button_text='Play',key='playbtn'), gui.Exit()]]

# Initialize window
window = gui.Window('Camera View')
window.Layout(layout).finalize()



while True:
    event, values = window.Read(timeout=0)
    if event == gui.WIN_CLOSED or event == 'Exit':
        break
    
    
    
window.close()