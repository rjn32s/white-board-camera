# white-board-camera
## Steup
````
pip install numpy
pip install opencv-python

````
## How to setup RaspBerryPi as RTSP Server
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

