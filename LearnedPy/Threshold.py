import cv2 as cv
import requests
import os

# To download an image from a URL
def download_image(url, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure directory exists
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded to {save_path}")
    else:
        print("Error: Could not download image.")

# Image URL and save path
image_url = "https://c8.alamy.com/comp/PG6R0G/usa-nyc-brooklyn-man-walking-in-the-street-holding-cup-of-coffee-PG6R0G.jpg"
save_path = "images/coffee_person.jpg"

# Download the image
download_image(image_url, save_path)

# Load and process the image
image = cv.imread(save_path)
if image is None:
    print("Error: Could not load image.")
else:
    # Create grayscale image
    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Thresholding
    _, thresh1 = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
    thresh2 = cv.adaptiveThreshold(gray_img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
    thresh3 = cv.adaptiveThreshold(gray_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

    # Add frame names to images
    windows = {
        'Gray Image': gray_img,
        'Binary': thresh1,
        'Thresh_mean': thresh2,
        'Thresh_gaussian': thresh3
    }

    for name, img in windows.items():
        # Add text to the image
        cv.putText(
            img,                       # Image to draw on
            name,                      # Text to display
            (10, 30),                  # Bottom-left corner of the text
            cv.FONT_HERSHEY_SIMPLEX,   # Font type
            1,                         # Font scale
            (160, 32, 260),           # Text color (white)
            5,                         # Thickness of text
            cv.LINE_AA                 # Line type
        )

        # Create and resize window
        cv.namedWindow(name, cv.WINDOW_NORMAL)
        height, width = img.shape[:2]
        cv.resizeWindow(name, width // 2, height // 2)
        cv.imshow(name, img)

    # Wait for 'q' key to exit
    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cv.destroyAllWindows()
