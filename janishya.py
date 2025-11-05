import cv2
from fer import FER

def main():
    # Initialize the FER detector
    detector = FER()
    
    # Start video capture from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB format for FER
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect emotions in the frame
        result = detector.detect_emotions(rgb_frame)

        # Draw bounding boxes and labels on the frame
        for face in result:
            (x, y, w, h) = face['box']
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            emotions = face['emotions']
            max_emotion = max(emotions, key=emotions.get)
            label = f"{max_emotion}: {emotions[max_emotion]:.2f}"
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('emotion', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()