import serial
import os
import random
import cv2
import numpy as np
import struct
import time
import sys
def main():
	args = sys.argv[1:]
	if len(args) == 2 and args[0] == '-port':
		port = str(args[1])	
	else:
		port = '/dev/ttyUSB1' # default port

	dims = (32,24) # dimensions of images to train/test with
	
	read_dir = '/data/' # path to test images
	
	number = ['0/','0/','0/','0/','1/','1/','1/','1/','2/','2/','2/','2/','3/','3/','3/','3/','4/','4/','4/','4/']
	
	list =['0008817_png.rf.506fea406cabcafbf0f51e357cd603d0.jpg',
			'0008836_png.rf.738861d6b132050c7f98f74d90129287.jpg',
			'0009671_png.rf.c0c816551c511d131c7ed0cf7925c5ad.jpg',
			'0008816_png.rf.615ccd2b03bc348ff397be46752e068b.jpg',
			'0010501_png.rf.dcb9e5f5c40e53065632ebb916caeca2.jpg',
			'0012211_png.rf.456953d733460763e6fbbd0f52b709e6.jpg',
			'0011393_png.rf.0a961a1b2d2a5cbbc51575d8010fe27b.jpg',
			'0011835_png.rf.465a89d5c5cf5a986f36e9ad36e7fccf.jpg',
			'0006194_png.rf.d42d65196711e6c2e8eecd7657ab6868.jpg',
			'0006186_png.rf.5e664ab0a7d3770268ac61035c7c8789.jpg',
			'0008725_png.rf.9caa8c1cdf186d307890ffec10c60e93.jpg',
			'img131_png.rf.962f96423c60fbbb126b445a5d824ccf.jpg',
			'0006741_png.rf.a5dc1c1fcff5b5b7686329a243dcbc2e.jpg',
			'0005092_png.rf.7521dd611038e5def2dec6578c3327fe.jpg',
			'0005019_png.rf.7cb57f919c6288950403663c63197905.jpg',
			'0006787_png.rf.2199f3fa034ab7169e02133845c01e2c.jpg',
			'0009750_png.rf.c643e64b7718b562beea86632688d6ab.jpg',
			'0009706_png.rf.67ebc57be8b0a49c51e79b835568783a.jpg',
			'0009883_png.rf.31931ffd9d1d60ec6de90c8e1ab8cbcf.jpg',
			'0009983_png.rf.fe79a44aff3ec523fd03def44ad28487.jpg']
	count = 0
	for read_file in list:
		img = cv2.imread(os.path.join(read_dir+number[count],read_file),0) # read img as grayscale
		
		imgrgb = cv2.imread(os.path.join(read_dir+number[count],read_file)) # read img as rgb
		
   
		img = cv2.resize(img, dims, interpolation = cv2.INTER_LINEAR)	# resize img to fit dims
		cv2.imshow('image',img) # show test image
		img = np.asarray((img / 255)).astype('float32')
		print("Label: ", number[count], " Filename: ", read_file, " Serialport: ", port) # print test image label
		# define serial connection
		ser = serial.Serial(port, 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

	
		file = open(read_file + ".txt", "w")
		for i in range(dims[1]):
			for j in range(dims[0]):
				values = bytearray(struct.pack("f", img[i][j])) # turn pixel values into bytearray
				#print(values)
				#time.sleep(0.01)
				ser.write(values) # send bytearray over UART
				sizeOfByteArray = len(values)
				#print(sizeOfByteArray)
				file.write(str(img[i][j]) + "\n") # write pixel values to file

		nn_res = number[count] # initialize nn_res
		while "output" not in nn_res: # check if nn output received
			nn_res = ser.readline().decode('UTF-8') # decode received bytes
			#print(nn_res) # can be used to display prints from U96
		
	
		print("Label {}".format(nn_res))
  
		""" if imgrgb is not None and imgrgb.shape[0] > 0 and imgrgb.shape[1] > 0:
			cv2.imshow(number[count]+nn_res, imgrgb)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
		else:
			print("Error: Failed to load the image.") """
		count += 1
	
	
if __name__=="__main__":
    main()
