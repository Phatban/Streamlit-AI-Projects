"""
object_detection.py

This module provides functions for object detection using OpenCV's DNN module.

Functions:
    process_image(image): Process an image using MobileNet-SSD model.
    annotate_image(image, detections, confidence_threshold): Annotate image with detected objects.

This module is part of the Object Detection project using Streamlit.
"""

import cv2
import numpy as np

MODEL = "model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "model/MobileNetSSD_deploy.prototxt.txt"


def process_image(image):
    """
    Process an image using MobileNet-SSD model.

    Args:
    image (numpy.ndarray): Input image.

    Returns:
    numpy.ndarray: Detections from the model.
    """
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    """
    Annotate image with detected objects.

    Args:
    image (numpy.ndarray): Input image.
    detections (numpy.ndarray): Detections from the model.
    confidence_threshold (float): Confidence threshold for detections.

    Returns:
    numpy.ndarray: Annotated image.
    """
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x_min, y_min, x_max, y_max) = box.astype("int")
            cv2.rectangle(image, (x_min, y_min),
                          (x_max, y_max), (0, 255, 0), 2)
    return image
