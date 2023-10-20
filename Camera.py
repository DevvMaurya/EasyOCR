import cv2
import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])  # You can specify the languages you want to recognize

# Initialize the camera capture
cap = cv2.VideoCapture(0)  # Use the default camera (usually the built-in webcam)

while True:
    flag = True
    ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUMBERS = '1234567890'
    INDEX = '0145'
    y = []
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Perform character recognition on the captured frame
    results = reader.readtext(frame)

    # Loop through the recognized text results and draw bounding boxes and text on the frame
    for (bbox, text, prob) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(frame, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    for text in results:
        temp = str(text[1])
        print(text[1])
        y = [x for x in temp]
        for index in range(len(temp)):
            if str(index) in INDEX:
                if y[index] not in ALPHABETS:
                    print("alphabet not in range")
                    flag = False
                    break
            else:
                if y[index] not in NUMBERS:
                    print("number not in range")
                    flag = False
                    break
                

    # Display the frame with recognized text
    cv2.imshow('Character Recognition', frame)

    # Break the loop if the 'q' key is pressed
    if flag is not False:
        print(''.join(y))
        break
    else:
        print("number error")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
