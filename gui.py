import PySimpleGUI as gui
import detector as det


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