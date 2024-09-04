# Author Uditya Narayan Tiwari

---

# OpenCV Project in Python

This repository contains various image and video processing tasks implemented using OpenCV in Python. It covers fundamental operations like image manipulation, filtering, edge detection, and video processing.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. This project demonstrates how to leverage OpenCV to perform common tasks in image and video processing.

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/opencv-project-python.git
cd opencv-project-python
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Creating a virtual environment helps in managing dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages, including OpenCV, using `pip`:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can install OpenCV directly:

```bash
pip install opencv-python
```

## Usage

### Basic Commands

1. **Read and Display an Image**:
   ```python
   import cv2
   img = cv2.imread('input.jpg')
   cv2.imshow('Image', img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

2. **Convert Image to Grayscale**:
   ```python
   img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   cv2.imwrite('output_gray.jpg', img_gray)
   ```

3. **Detect Edges in an Image**:
   ```python
   edges = cv2.Canny(img_gray, 100, 200)
   cv2.imwrite('output_edges.jpg', edges)
   ```

### Running Scripts

Run any of the scripts provided in the repository using:

```bash
python script_name.py
```

Replace `script_name.py` with the name of the script you want to execute.

## Features

- Image reading and writing
- Grayscale conversion
- Edge detection
- Video capture and processing
- Object detection and tracking
- Image filtering (Gaussian, Median, etc.)

## Examples

### Example 1: Video Capture from Webcam

Capture video from the webcam and display it:

```python
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Example 2: Face Detection using Haar Cascades

Detect faces in an image:

```python
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('input.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imwrite('output_faces.jpg', img)
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
