# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:17:34 2018

@author: javi
"""
import subprocess
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

import boto3
from inotify_simple import INotify, flags
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from datetime import date, datetime
import json
import cv2
from uuid import getnode as get_mac
import time
import psycopg2


import fnmatch, os







#os.system(' tvservice -o')
os.system(' mkdir capture')

mac = get_mac()
print (mac)
s3 = boto3.client('s3', aws_access_key_id= open('keys.txt').readline().split(None, 1)[0],
aws_secret_access_key= open('keys.txt').readlines()[1].split(None, 1)[0])




timestr = time.strftime("%Y-%m-%d-%H:%M:%S")

while 1:
        cam = cv2.VideoCapture(0)


        timestr = time.strftime("%Y-%m-%d-%H:%M:%S")
        ret, image = cam.read()
        cv2.imwrite('capture/image-'+timestr+'.jpg',image,[int(cv2.IMWRITE_JPEG_QUALITY), 50])
        print("image written go to sleep")
        cam.release()

        time.sleep(10)   # Delays for 5 seconds. You can also use a float value.

        
        
        
        
        
        
        
        
        
        
        
        
