import cv2
import os

# Read the image
image_path = os.path.join('.','images', 'david.jpg')
image = cv2.imread(image_path)

# Save the processed image
cv2.imwrite(os.path.join('.','images', "david_out.jpg"), image)

# Create and resize the window
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)  # Create a named window
cv2.resizeWindow('frame', 100, 100)  # Resize the window

# Display the image
cv2.imshow('frame', image)
cv2.waitKey(0) 

# Close all OpenCV windows
cv2.destroyAllWindows()
