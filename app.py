import cv2

# Loading image from a file
image = cv2.imread('girl.jpeg')

if image is None:
    print("Error girl.jpeg not found")
else:    
    # Displaying an img in a Window
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Converting an img to grayscale form
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Displaying the grayscale image
cv2.imshow('Gray Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Edge Detection
# Applying Canny edge detection

edges = cv2.Canny(gray_img, 50, 150)

# Displaying the edge detected image
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

