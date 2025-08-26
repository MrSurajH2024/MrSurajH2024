import cv2
import os 

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
face_detector = cv2.CascadeClassifier('F:/python/frp/haarcascade_frontalface_default.xml') 
face_id = input('\n enter user id end press <return> ==> ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

count = 0
#nameID = str(input("Enter Your Name: ")).lower()
'''path = 'F:/python/frp/dataset/'
isExist = os.path.exists(path)

if isExist:
    print("Name Already Taken")
    nameID = str(input("Enter your name Again"))
else:
    os.makedirs(path)'''

while(True):
    ret, img = cam.read()
   # img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),2)
        count += 1
        # save the captured image into the dataset Folder
        '''name = '/images/'+ nameID + '/' + str(count) + '.jpg',
        print("Creating images......."+name)'''
        
        cv2.imwrite("F:/python/frp/dataset/Harsha. " + str(face_id) +'.' +  str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('Faster', img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    #take 30 face sample and stop video
    elif count >= 30:
        break
#do a bit of cleanup 
print("\n [INFO] Existing Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows() 
