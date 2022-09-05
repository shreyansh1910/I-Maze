#PS2_CONTROLER_BY_RoboPirates
from controller import Robot,DistanceSensor,Camera,Motor
import numpy as np
import cv2,time

robot= Robot()
#DEFINING COLOR RANGE
    #COLOR CODES
    #GREEN = 0
    #BLUE = 1
    #VOILET = 2
    #RED =3
def color_range(i):
    if i==0:#GREEN
        llimit=np.array([60,45,45])
        ulimit=np.array([100,255,255])
    elif i==1:#BLUE
        llimit=np.array([115,95,95])
        ulimit=np.array([140,255,255])
    elif i==2:#VOILET
        llimit=np.array([130,50,50])
        ulimit=np.array([160,255,255])
    elif i==3:#RED
        llimit=np.array([160,50,50])
        ulimit=np.array([180,255,255])
    return (llimit,ulimit)

timestep = int(robot.getBasicTimeStep())
max_speed=6.28

left_motor=robot.getDevice('left wheel motor')
right_motor=robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

camera=robot.getDevice('camera')
camera.enable(timestep)
prox_sensor=[]
for i in range(8):
    temp='ps'+str(i)
    prox_sensor.append(robot.getDevice(temp))
    prox_sensor[i].enable(timestep)


def getContAndWid():
    camera.saveImage("hello.png",25)
    image = cv2.imread("hello.png")
    height,width,chanels=image.shape
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower,upper=color_range(color)
    mask=cv2.inRange(hsv,lower,upper)
    contour,nt=cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return mask,contour,width

def stop():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    print('TASK COMPLETED BY RoboPirates ROBOT IN : ',str(robot.getTime()),'SEC')

def moveBack():#MOVE BACK FUNCTION
    t=time.time()
    while time.time()-t<=1:
        left_motor.setVelocity(-max_speed/2)
        right_motor.setVelocity(-max_speed/2)
        robot.step(timestep)
        pass   
def moveLeft(speed):#MOVE RIGHT FUNCTION
    if(speed>100):
        speed=100
    speed=(max_speed/100.0)*speed
    for _ in range(10):
            left_motor.setVelocity(-speed)
            right_motor.setVelocity(speed)

            
def moveRight(speed):#MOVE RIGHT FUNCTION
    if(speed>100):
        speed=100
    speed=(max_speed/100.0)*speed
    for _ in range(10):
            left_motor.setVelocity(speed)
            right_motor.setVelocity(-speed)

            
def moveForward():#MOVE FORWARD FUNCTION
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(max_speed)


#since we are using camera piixel 512 x 512 so maximum sum of contor will be 262144
#to check if the bot is near any contor we can approx 80% of max i.e = 209000
    #COLOR CODES
    #GREEN = 0
    #BLUE = 1
    #VOILET = 2
    #RED =3
color=0 #STRTING FROM GREEN
while robot.step(timestep)!=-1:
    frontr= prox_sensor[0].getValue()
    right = prox_sensor[1].getValue()
    left = prox_sensor[6].getValue()
    frontl = prox_sensor[7].getValue()
    
    mask,contour,width=getContAndWid()
    pix_sum=np.sum(mask)/255
    if left > 100 or frontl > 85:
        i=time.time()
        while time.time()-i<0.3:
         left_motor.setVelocity(3)
         right_motor.setVelocity(-3)
         robot.step(timestep)
        pass
        i=time.time()
        while time.time()-i<1:
         left_motor.setVelocity(4)
         right_motor.setVelocity(4)
         robot.step(timestep)
        pass
      
        i = time.time()
        while time.time()-i<0.8:
         left_motor.setVelocity(-3)
         right_motor.setVelocity(3)
         robot.step(timestep)
        pass
    if right > 100 or frontr>85:
        i=time.time()
        while time.time()-i<0.3:
         left_motor.setVelocity(-3)
         right_motor.setVelocity(3)
         robot.step(timestep)
        pass
        i=time.time()
        while time.time()-i<1:
         left_motor.setVelocity(4)
         right_motor.setVelocity(4)
         robot.step(timestep)
        pass
      
        i = time.time()
        while time.time()-i<0.8:
         left_motor.setVelocity(3)
         right_motor.setVelocity(-3)
         robot.step(timestep)
        pass
    if pix_sum>350:
        for i in range(len(contour)):
            area=cv2.contourArea(contour[i])
            if area>400:
                ct=contour[i]
        M=cv2.moments(ct)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        if cx >=(width*9)/20 and cx <=(width*11)/20:
            if pix_sum>209000:
                color+=1
                if color>3:#autonomus stop and exit block
                    stop()
                    break
                moveBack()
            moveForward()
        elif cx >(width*11)/20:
            left_motor.setVelocity(6.2)
            right_motor.setVelocity(4)

        elif cx<(width*9)/20:
            left_motor.setVelocity(4)
            right_motor.setVelocity(6.2)

    else:
        init=time.time()
        while time.time()-init<4:
            moveRight(50)
            mask,contour,width=getContAndWid()
            if np.sum(mask)/255 >500:
                break
            robot.step(timestep)
            pass
            
        init=time.time()
        while time.time()-init<3:
            moveForward()
            mask,contour,width=getContAndWid()
            if np.sum(mask)/255 >500:
                break
            robot.step(timestep)
            pass
        init=time.time()
        while time.time()-init<0.5:
            moveRight(50)
            mask,contour,width=getContAndWid()
            if np.sum(mask)/255 >500:
                break
            robot.step(timestep)
            pass
    pass