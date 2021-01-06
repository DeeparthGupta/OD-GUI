import PySimpleGUI as gui
from Detector import Detector
from InputStream import InputStream



# detector = Detector('yolo_support_files', size=vid_size #Create a detector 

vid_size = (320,320)

layout = [
    [gui.Text('YOLO Video Player', size=(22,1), font=('Any',18),text_color='#ffffff' ,justification='center')],
    [gui.Text('Path to input video'), gui.In(size=(40,1), key='input'), gui.FileBrowse()],
	# [gui.Text('Path to output video'), sg.In(o_vid,size=(40,1), key='output'), sg.FileSaveAs()],
	[gui.Text('Minimum Confidence'),gui.Slider(range=(0,1),orientation='h', resolution=.1, default_value=.5, size=(15,15), key='confidence')],
	[gui.OK(), gui.Exit()]
 ]

# Layout of the popup window
layout1 = [[gui.Image(key='videoOut',tooltip='Video goes here.', size=vid_size)],
          [gui.ReadButton(button_text='Play',key='playbtn'), gui.Exit()]]

# Initialize window
window = gui.Window('Object detector')
window.Layout(layout).finalize()




while True:
    event, values = window.Read(timeout=0)
    if event == gui.WIN_CLOSED or event == 'Exit':
        break

    
window.close()