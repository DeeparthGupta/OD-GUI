from detector import Detector
import PySimpleGUI as gui
import Detector as det


detector = Detector('yolo_support_files', size=(320,320))

layout = [[gui.Image(filename='', key='videoOut',tooltip='Video goes here.', size=(480,320))],
          [gui.ReadButton(button_text='Play',key='playbtn'), gui.Exit()]]

window = gui.Window('Camera View')
window.Layout(layout).finalize()

stopped = 0



while True:
    event, values = window.Read(timeout=0)
    if event == gui.WIN_CLOSED or event == 'Exit':
        break
    
    
    
window.close()