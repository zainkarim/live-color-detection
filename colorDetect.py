import cv2
import numpy
'''
# Red
lower = numpy.array([0, 150, 35])
upper = numpy.array([12, 255, 255])

# Orange
lower = numpy.array([12, 150, 35])
upper = numpy.array([25, 255, 255])

# Yellow
lower = numpy.array([26, 150, 35])
upper = numpy.array([35, 255, 255])

# Green
lower = numpy.array([36, 150, 20])
upper = numpy.array([80, 255, 255])

# Blue
lower = numpy.array([86, 150, 20])
upper = numpy.array([120, 255, 255])

# Purple
lower = numpy.array([121, 150, 20])
upper = numpy.array([140, 255, 255])

# Black
lower = numpy.array([0, 150, 0])
upper = numpy.array([255, 255, 50])

'''

# Declare lower and upper values of color to be detected in HSV

# Blue
lower = numpy.array([86, 150, 20])
upper = numpy.array([120, 255, 255])

# Read in video feed
video = cv2.VideoCapture(0)

# Run process endlessly with while loop
while True:
    # Read video opbject, determine whether or not video was read succesfuly and store boolean in 'success', and new image in 'img'
    success, image_in = video.read()
    # Convert footage to HSV
    image_out = cv2.cvtColor(image_in, cv2.COLOR_BGR2HSV)
    # Create mask object to find and seperate the determined color from the original image
    mask = cv2.inRange(image_out, lower, upper)

    # Detect contours into two variables
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check length of contours 
    if len(contours)!= 0:
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image_in, (x,y), (x + w, y + h), (0, 255, 0), 2)


    # Display both original and masked image
    cv2.imshow("mask", mask)
    cv2.imshow("webcam",image_in)

    # Wait for a key event
    key = cv2.waitKey(1)

    # Check if 'q' key was pressed
    if key == ord('q'):
        # Terminate the program
        break

# Destroy all windows
cv2.destroyAllWindows()