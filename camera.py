import cv2
import numpy as np
import time



def vid():
    cap = cv2.VideoCapture(0)
    timestr = time.strftime('%H%M%S', time.localtime())

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('butts %s.mp4' % timestr, fourcc, 20.0, (640,480))

    
    while time.time() < starttime + 3:
        cap.open()
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

    cap.release()
    out.release()

def pic(cam_addr):
    cam = cv2.VideoCapture(cam_addr)
    starttime = time.time()

    for i in range(30):
        success, image = cam.read()
    
    timestr = time.strftime('%H-%M-%S', time.localtime())
    if success:
        cv2.imwrite('picsnap %s.jpg' % timestr, image)
        print('*****PIC TAKEN at cam address %d' % cam_addr)
    else:
        print('No Camera at cam address %d' % cam_addr)
    cam.release()

    

pic(0)

        
