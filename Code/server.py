
#  
# SERVER SIDE CODE (Rasberry PI .py file which will send the video frame using the TCP Protocol)
#
import socket, cv2, pickle,struct,imutils

# Socket Create
#####################################################################################
#####################################################################################
# This code from line 11 to 24 is standard code taken from Python documenation page.
# ref link : https://docs.python.org/3/library/socket.html
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)
#######################################################################################3
########################################################################################
# Once the handshaking is Done 
# We will start the Captruring the frame
# The frame will be tranmitted as the Bit stream with the help of pickel library
# At the client side this bit stream will get deserialized and convereted back into image
# Socket Accept Code
while True:
	client_socket,addr = server_socket.accept()
	print('GOT CONNECTION FROM:',addr) # Client Address
	if client_socket:
		#vid = cv2.VideoCapture('http://192.168.0.104:8080/video')

		vid = cv2.VideoCapture(0)# For taking the video frames from webcam
		while(vid.isOpened()):
			img,frame = vid.read()
			frame = imutils.resize(frame,width=800) # Resize the frame for low latency This is optional step
			a = pickle.dumps(frame) # Serializing the frames into bit stream of 0 1
			message = struct.pack("Q",len(a))+a  # Disconnection Code if Pressed 'Q' the connection will get terminated
			# Sending the Frame to the client
			client_socket.sendall(message)
			
			#cv2.imshow('TRANSMITTING VIDEO',frame)
			# If we want to terminated the process from Serever side then press 'Q'.
			# This step is optional
			key = cv2.waitKey(1) & 0xFF
			if key ==ord('q'):
				client_socket.close()
