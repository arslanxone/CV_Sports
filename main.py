import cv2

def pre_processing(image):
    '''
    Return:
        processed_image: Mandatory pre processing steps to get the better results from OCR.
    Parameters:
        image: image needed to be processed. 
    '''
    #converting it to the grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #applying thresholding
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    return thresh


video_path = '../sample_1.mp4' #change path of the video where you downloaded in the PC
cap = cv2.VideoCapture(video_path)
pre_ret, pre_image = cap.read()
pre_image_thresh = pre_processing(pre_image)

while True: 
    ret, image = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break    
    
    image_thresh = pre_processing(image)

    img_bwo = cv2.bitwise_or(pre_image_thresh, image_thresh)
    
    pre_image_thresh = image_thresh

    cv2.imshow('bwo_output', img_bwo)
    if cv2.waitKey(1) & 0xFF == ord('q'):               
        break

cap.release()
cv2.destroyAllWindows() 