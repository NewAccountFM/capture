# import OpenCV
import cv2



def myfunc(i):
    pass

cv2.namedWindow('title')

cv2.createTrackbar('value', 'title', 0, 200, myfunc)

# create instanceVideoCapture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
while True:
# read a frame
    ret, frame = cap.read()



    
    
    v = cv2.getTrackbarPos('value','title')
    v = v / 100
    
    frame[:,:,0] = 255*((frame[:,:,0]/255) ** v)
    frame[:,:,1] = 255*((frame[:,:,1]/255) ** v)
    frame[:,:,2] = 255*((frame[:,:,2]/255) ** v)
    
    
    # show image
    cv2.imshow('title', frame)
    


    # wait for user input for 1ms
    # when the esc key input, break 
    k = cv2.waitKey(1)
    if k == 27:
        break

# release and close all windows
cap.release()
cv2.destroyAllWindows()
