import cv2

# Open a video capture object
cap = cv2.VideoCapture(r'd:\Covering Python Basics for Minor Project\OpenCV Py\Video processing\timelapse.mp4')

if not cap.isOpened():
    print("Error: Couldn't open the video")
    exit()

# Loop through the video frames
while True:
    # Read a frame from a video
    ret, frame = cap.read()

    #Break the loop is the video ends
    if not ret:
        break

    #Display the original frame
    cv2.imshow("Original Video", frame)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Black and White Video", gray_frame)

    #Perform edge dection on the video
    edges_frame = cv2.Canny(gray_frame, 50, 150) 
    # Edges with intensity gradient higher than 150 are considered strong edges.
    # Edges with intensity gradient lower than 50 are discarded.
    cv2.imshow("Edges Video", edges_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()