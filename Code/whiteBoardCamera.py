import numpy as np
import cv2


class Camera:
    def __init__(self):
        self.addr = "rtsp://192.168.0.106:8554/unicast"
        #self.userconcent()
        self.cam = cv2.VideoCapture(self.addr)
        _,self.img = self.cam.read()
    def showfeed(self):
        return self.cam.read()
    def stopfeed(self):
        self.cam.release()
    def firtstImage(self):
        return self.img
    def correction(self,frame,M):
        hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)            
        ch = cv2.equalizeHist(v)
        limg = cv2.merge((h,s,ch))
        final = cv2.cvtColor(limg, cv2.COLOR_HSV2BGR)
        image = cv2.cvtColor(final, cv2.COLOR_BGR2RGB) 
        dst = cv2.warpPerspective(frame,M,(640,400))
        dst = cv2.GaussianBlur(dst,(5,5),0)
        dst = cv2.bilateralFilter(dst,1,50,50)
        return dst
    def userconcent(self):
        id=input("Continue with study mode [y/n] : ")
        
        if id.lower() == 'n':
            self.addr = int(input("Enter the Raspberry RTSP SERVER LINK : "))
        else:
            self.addr = "rtsp://192.168.0.106:8554/unicast"
        

if __name__ == '__main__':
    
    ASPECT_RATIO = (500,707)
    pts2 = np.float32([[0,0],[ASPECT_RATIO[1],0],[0,ASPECT_RATIO[0]],[ASPECT_RATIO[1],ASPECT_RATIO[0]]])
    pointIndex = 0
    pts = [(0,0),(0,0),(0,0),(0,0)]
    myWhiteBoard = Camera()
    def draw_circle(event,x,y,flags,param):
        img = myWhiteBoard.firtstImage()
        global pointIndex
        global pts
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img,(x,y),5,(0,0,0),-1)
            pts[pointIndex] = (x,y)
            pointIndex = pointIndex + 1
    def selectFourPoints():
        img = myWhiteBoard.firtstImage()
        global pointIndex
        while(pointIndex != 4):
            cv2.imshow('image',img)
            key = cv2.waitKey(20) & 0xFF
            if key == 27:
                return False
        return True
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)
    myWhiteBoard.showfeed()
    if selectFourPoints():
        pts1 = np.float32([[pts[0][0],pts[0][1]],[pts[1][0],pts[1][1]],[pts[2][0],pts[2][1]],[pts[3][0],pts[3][1]] ])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        cv2.destroyAllWindows()
        cam = cv2.VideoCapture("rtsp://192.168.0.106:8554/unicast")
        while True:
            _,frame=cam.read() #myWhiteBoard.showfeed()
            dst = myWhiteBoard.correction(frame,M)
            cv2.imshow("OUTPUT FEED",dst)
            key = cv2.waitKey(10) & 0xFF
            if key == 27:
                break
    else:
        print("Exit")
    myWhiteBoard.stopfeed()
cv2.destroyAllWindows()