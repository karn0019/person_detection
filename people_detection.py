import cv2
import numpy as np
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
id=0 
cv2.startWindowThread()
 
# เปิดเว็บแคม
cap = cv2.VideoCapture('vid5.mp4')
 
# อีดวิดิโอ
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (1280,720))
 
while(True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
  
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
 
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
 
    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
        cv2.putText(frame,'Person',(xA,yA-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),1)
    out.write(frame.astype('uint8'))
    id=id+1
    id_text=str(id)
    filename='pic'
    sur='.jpg'
    cv2.imwrite(filename+id_text+sur,frame)
     
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
 
cap.release()
out.release()
 
cv2.destroyAllWindows()
cv2.waitKey(1)
