import cv2 as cv
import os
import requests

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded to {save_path}")
    else:
        print("Error: Could not download image.")

image_url = "Enter your image URL here"
save_path = "images/downloaded_image.jpg"

download_image(image_url, save_path)

image = cv.imread(save_path)
if image is None:
    print("Error: Could not load image.")
else:
    cv.imshow('Downloaded Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()