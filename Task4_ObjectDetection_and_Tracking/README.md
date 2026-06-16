# CodeAlpha Object Detection and Tracking

This project performs real-time object detection and tracking using YOLOv8 and OpenCV. The system captures live video from a webcam, detects objects, draws bounding boxes, and assigns tracking IDs to each detected object.

## Features

* Real-time webcam video processing
* Object detection using YOLOv8
* Bounding box visualization
* Object tracking with ByteTrack
* Tracking IDs for detected objects
* Confidence score display

## Technologies Used

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* ByteTrack

## Installation

Install the required libraries:

```bash
pip install ultralytics opencv-python
```

## Run the Project

```bash
python object_detection.py
```

Press **Q** to quit the application.

## Output

* Detects objects in real time
* Displays object labels
* Shows confidence scores
* Assigns unique tracking IDs
* Draws bounding boxes around detected objects

Developed as part of the CodeAlpha Artificial Intelligence Internship.
