import cv2

vc = cv2.VideoCapture(0) # Open the camera. # 0 represents the default camera (usually the built-in webcam)

def detect(gray, frame): 
	faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
	for (x, y, w, h) in faces: 
		cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2) 
		roi_gray = gray[y:y + h, x:x + w] 
		roi_color = frame[y:y + h, x:x + w] 
		smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 

		for (sx, sy, sw, sh) in smiles: 
			cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
	return frame 

if __name__ == "__main__" :
    video_capture = cv2.VideoCapture(0) 
    while video_capture.isOpened(): 
    # Captures video_capture frame by frame 
        _, frame = video_capture.read()  
    
        # To capture image in monochrome                     
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml') 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            print("No face detected")

        if len(faces) > 1:
            print("Multiple faces detected")
        
        smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml') 
        
        # calls the detect() function     
        canvas = detect(gray, frame)    
    
        # Displays the result on camera feed                      
        cv2.imshow('Video', canvas)  
    
        # The control breaks once q key is pressed                         
        if cv2.waitKey(1) & 0xff == ord('q'):                
            break
    
    # Release the capture once all the processing is done. 
    video_capture.release()                                  
    cv2.destroyAllWindows() 
