from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO



camera = PiCamera()
camera.resolution = (300, 240)
rawCapture = PiRGBArray(camera, size=(300, 240))
time.sleep(0.1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(7, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)

kernel = np.ones((3,3), np.uint8)
x_last = 100
y_last = 80

start_time=time.time()
counter=0


kp=.75
ap=1
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):  
    image = frame.array
    counter+=1
    Blackline = cv2.inRange(image, (0,0,0), (75,75,75)) 
    
    Blackline = cv2.erode(Blackline, kernel, iterations=7)
    Blackline = cv2.dilate(Blackline, kernel, iterations=9) 
    contours_blk, hierarchy_blk = cv2.findContours(Blackline.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    contours_blk_len = len(contours_blk)
    if contours_blk_len > 0 :
     if contours_blk_len == 1 :
      blackbox = cv2.minAreaRect(contours_blk[0])
     else:
       canditates=[]
       off_bottom = 0      
       for con_num in range(contours_blk_len):      
        blackbox = cv2.minAreaRect(contours_blk[con_num])
        (x_min, y_min), (w_min, h_min), ang = blackbox      
        box = cv2.cv.BoxPoints(blackbox)
        (x_box,y_box) = box[0]
        if y_box > 118 :         
         off_bottom += 1
        canditates.append((y_box,con_num,x_min,y_min))      
       canditates = sorted(canditates)
       if off_bottom > 1:       
        canditates_off_bottom=[]
        for con_num in range ((contours_blk_len - off_bottom), contours_blk_len):
           (y_highest,con_highest,x_min, y_min) = canditates[con_num]       
           total_distance = (abs(x_min - x_last)**2 + abs(y_min - y_last)**2)**0.5
           canditates_off_bottom.append((total_distance,con_highest))
        canditates_off_bottom = sorted(canditates_off_bottom)         
        (total_distance,con_highest) = canditates_off_bottom[0]         
        blackbox = cv2.minAreaRect(contours_blk[con_highest])      
       else:        
        (y_highest,con_highest,x_min, y_min) = canditates[contours_blk_len-1]       
        blackbox = cv2.minAreaRect(contours_blk[con_highest])    
     (x_min, y_min), (w_min, h_min), ang = blackbox
     x_last = x_min
     y_last = y_min
     if ang < -45 :
      ang = 90 + ang
     if w_min < h_min and ang > 0:    
      ang = (90-ang)*-1
     if w_min > h_min and ang < 0:
      ang = 90 + ang      
     setpoint = 320
     error = int(x_min - setpoint) 
     ang = int(ang)
     #Motor_steer (BP.PORT_A, BP.PORT_D,82, (error*kp)+(ang*ap))
     box = cv2.cv.BoxPoints(blackbox)
     box = np.int0(box)
     cv2.drawContours(image,[box],0,(0,0,255),3)     
     cv2.putText(image,str(ang),(10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
     #print (ang)
     if ((ang)>=-10) & ((ang)<=10):
      GPIO.output(16, GPIO.LOW)     ##RIGHT FORWARD
      GPIO.output(18, GPIO.LOW)     ##LEFT FORWARD
     elif ((ang)>=40) & ((ang)<=60):
      GPIO.output(18, GPIO.LOW)
      GPIO.output(16, GPIO.HIGH)
     elif ((ang)>=60) & ((ang)<=80):
      GPIO.output(16, GPIO.LOW)     ##RIGHT FORWARD
      GPIO.output(18, GPIO.LOW)     ##LEFT FORWARD
     elif ((ang)>=-40) & ((ang)<=-80):
      GPIO.output(16, GPIO.LOW)
      GPIO.output(18, GPIO.HIGH)
     else:    
      GPIO.output(16, GPIO.HIGH)
      GPIO.output(18, GPIO.HIGH)
     cv2.putText(image,str(error),(10, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
     cv2.line(image, (int(x_min),90 ), (int(x_min),110 ), (255,0,0),3)
     
        
    cv2.imshow("orginal with line", image)  
    rawCapture.truncate(0)  
    key = cv2.waitKey(1) & 0xFF 
    if key == ord("q"):
        break

