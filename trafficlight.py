import cv2

smokeCascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")


def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    feature=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords=[]
    for(x,y,w,h) in feature:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1)
    return img

def detect(img,faceCascade):
  
    img=draw_boundary(img,smokeCascade,1.2,1,(0,0,255),'person')
    return img

cap = cv2.VideoCapture("vid3.mp4")


while (True):
        ret,frame = cap.read()
        frame=detect(frame,smokeCascade)
        cv2.imshow('frame',frame)
        if (cv2.waitKey(1) & 0xFF== ord('q')):
            break
cap.release()
cv2.destroyAllWindows()
