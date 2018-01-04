# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 05:50:58 2017

@author: user
"""
import time
import rospy
# ROS Image message
from sensor_msgs.msg import Image
from std_msgs.msg import Float32, Int32
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except:
        e = CvBridgeError
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
        cv2.imwrite('camera_image.jpg', cv2_img)
        time.sleep(5)
def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/cameras/left_hand_camera/image"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    with open('camera_image.jpg', 'r+') as f:
       jpgdata = f.read()
       f.close()
       
    
    answer = Int32()
    rospy.Publisher("answer", Int32,answer.data)
    rospy.spin()
    
    
    

if __name__ == '__main__':
    main()