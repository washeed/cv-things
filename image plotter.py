import cv2

def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked coordinates: ({x}, {y})")

def get_clicked_coordinates(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Create a window and bind the mouse callback function
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", get_coordinates)

    # Display the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the path to the image file
image_path = 'inf.jpg'

# Call the function to get the clicked coordinates
get_clicked_coordinates(image_path)
