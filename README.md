# white-board-camera
## Supervisor 
Dr. Srikanth Sugavanam(https://github.com/SrikanthS-IIT)
![alt text](https://github.com/rjn32s/white-board-camera/blob/main/res/Final%20(1).png)
## Introduction
Because online education has become the new normal, technological ad-
vancements in the field of online education are required. It will become a
part of education because we will be able to continue our education from the
comfort of our own homes as needed. It also allows us to reach a broader
range of students. Most lectures are now videotaped with a camera and
a whiteboard. Issues such as Keystone’s perspective and uneven bright-
ness, on the other hand, contribute to the poor quality of online learning.
This project aims to solve this problem by developing a Raspberry PI-based
device that can be attached to the side or top of a whiteboard. It is a stand-
alone device that captures the whiteboard and transmits it to the valid user.
## Setup
### Client Side
````
pip install numpy
pip install opencv-python
pip install imutils

````
### Server Side
### How to setup RaspBerryPi as RTSP Server
If you want to use RaspberrPi as RTSP server insted of using server.py file then following command will setup the RaspberrPi in Headless Mode as RTSP server.
(type these command in Raspberrpi command terminal)
First setup some Basic library required.

````
sudo apt-get install caca-utils -y
````
Now Install v4l2rtspserver

````
sudo apt-get install cmake liblog4cpp5-dev libv4l-dev git -y
````
Once the packages are installed we can download the repository and build the source.

````
git clone https://github.com/mpromonet/v4l2rtspserver.git ; cd v4l2rtspserver/ ; cmake . ; make ; sudo make install
````
Start video stream

````
v4l2rtspserver -W 640 -H 480 -F 15 -P 8554 /dev/video0
````
## 3D Printable Object
![alt text](https://github.com/rjn32s/white-board-camera/blob/main/res/Case.gif)
