import cv2 as cv
import requests

image_path = 'https://images.pexels.com/photos/1661179/pexels-photo-1661179.jpeg?cs=srgb&dl=pexels-roshan-kamath-793618-1661179.jpg&fm=jpg'
img_data = requests.get(image_path).content
with open("images/bird.jpg",'wb') as handler:
    handler.write(img_data)

image = cv.imread("images/bird.jpg")

if image is None:
    print("Your image is not read")
else:
    print(image.shape)
    img_rgb = cv.cvtColor(image,cv.COLOR_BGR2RGB)
    gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    hsv_image = cv.cvtColor(image , cv.COLOR_BGR2HSV)


    cv.namedWindow('BGR_image',cv.WINDOW_NORMAL)
    cv.namedWindow('HSV_image',cv.WINDOW_NORMAL)
    cv.namedWindow('RGB_image',cv.WINDOW_NORMAL)
    cv.namedWindow('GRAY_image',cv.WINDOW_NORMAL)

    while True:
        cv.resizeWindow('BGR_image', 100, 100)
        cv.resizeWindow('RGB_image', 100, 100)
        cv.resizeWindow('GRAY_image', 100, 100)
        cv.resizeWindow('HSV_image', 100, 100)
    #visualize the image
        cv.imshow('BGR_image',image)
        cv.imshow('HSV_image',hsv_image)
        cv.imshow('GRAY_image',gray_image)

        cv.imshow('RGB_image',img_rgb)
            
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()


