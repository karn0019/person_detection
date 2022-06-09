import cv2
import os
cam =cv2.VideoCapture('output.avi') #import video

try:
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error : Creating directory of data')

currentframe = 0
#อ่านภาพในวิดิโอ
while(True):
    ret,frame=cam.read()

    if ret:
        name='./data/frame'+str(currentframe)+'.jpg'  
        print('Creating...'+name)

        cv2.imwrite(name,frame)

        currentframe += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()
        
