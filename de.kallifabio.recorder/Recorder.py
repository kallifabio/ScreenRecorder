import cv2, numpy, pyautogui, keyboard, os
from datetime import *

# directory = "videos"
# parent_dir = "DatenPascal/Programmieren/Python/ScreenRecorder"
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
filename = "record"
screen_size = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*'mp4v')
vid = cv2.VideoWriter(filename + '-' + datetime.today().strftime("%d.%m.%Y") + '-' + datetime.today().strftime("%H.%M.%S") + '.mp4', codec, 30.0, (screen_size))

print('Starte Aufnahme')
while True:
    img = pyautogui.screenshot()
    numpy_frame = numpy.array(img)
    frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)
    vid.write(frame)
    if keyboard.is_pressed('x'):
        print('Stoppe Aufnahme')
        break

cv2.destroyAllWindows()
vid.release()