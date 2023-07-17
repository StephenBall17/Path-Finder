import cv2
import pyautogui
from win32api import GetSystemMetrics
import time
import numpy as np

width = GetSystemMetrics(0)
height = GetSystemMetrics(0)

dim = (width,height)

f = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("test.mp4",f,30.0,dim)

now_time = time.time()

dur = 10

end_time = now_start_time + dur

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1,cvf2.COLOR_BGR2RGB)

    output.write(frame)
    
    c_time = time.time()

    if c_time > end_time:
        break
output.release()
print("--- End ---")