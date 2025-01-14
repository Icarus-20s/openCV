import os
import cv2 as cv

image_path = os.path.join('.', 'images', 'david.jpg')
image = cv.imread(image_path)

if image is None:
    print("Your image is not read")
else:
    print(image.shape)
    # Cropping the image
    cropped_image = image[400:1000, 100:1400]

    print(cropped_image.shape)
    
    # Creating and resizing windows
    cv.namedWindow('Original Image', cv.WINDOW_NORMAL)
    cv.namedWindow('Cropped Image', cv.WINDOW_NORMAL)
    cv.resizeWindow('Original Image', 300, 300)
    cv.resizeWindow('Cropped Image', 300, 300)
    
    # Displaying the images
    while True:
        cv.imshow('Original Image', image)
        cv.imshow('Cropped Image', cropped_image)
        
        # Exit loop when 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cv.destroyAllWindows()
