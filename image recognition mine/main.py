import numpy #needed for proper functionning of opencv
import cv2 as cv #as cv means you dont have to write cv2.labalab instead cv.lablab maybe!

#img reading
"""img = cv.imread('image recognition mine/images/nebula pic.jpeg')    #reads/import image from memory
cv.imshow('imgggggg',img)                                           #opens image in another window
cv.waitKey(0)                                                       #timer for showing image (0=infinite time) maybe
"""

#video reading
livecam = cv.VideoCapture(0) #0 means the webcam of device,1 means first accesory camera attached and so on 2,3,4.. also, you can put addres of videos in 'address' for recorder video
    #error (-255)mean video ran out of frames
while True:
    istrue, frame = livecam.read()                                  #reads each frame of video one by one 

    cv.imshow('video', frame)                                       #displayes each frame

    if cv.waitKey(20) & 0xff == ord('q'): #and 0xff==ord('d'):      #if 20 time has passed and 'q' key is pressed the it will break loop and stop displaying frames
        break
capture.release()                                                   # release the captured frames ???
cv.destroyAllWindows()                                              #collapses all the current windows