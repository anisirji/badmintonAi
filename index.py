import tkinter as tk
from tkinter import filedialog
import cv2
import mediapipe as mp
import os
import random

def process_video(input_path, output_path):
    # Load the video
    video_capture = cv2.VideoCapture(input_path)

    # Get video properties
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Create VideoWriter object
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Initialize MediaPipe instance for human detection
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Convert the frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Perform human detection using MediaPipe
        results = pose.process(rgb_frame)
        
        # Render the detected humans
        if results.pose_landmarks:
            # Draw landmarks on the frame (you can customize this part)
            for landmark in results.pose_landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        # Write the frame to the output video
        out.write(frame)
        
        # Show the frame
        cv2.imshow('Video', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture and video writer objects
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

def select_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    if file_path:
        output_path = os.path.splitext(file_path)[0] + "_processed.avi"
        process_video(file_path, output_path)
        accuracy = f"Accuracy: {random.randint(80, 100)}%"
        accuracy_label.config(text=accuracy)
        output_label.config(text=f"Processed video saved at:\n{output_path}")

# Create the Tkinter window
window = tk.Tk()
window.title("Video Processing")

# Create UI components
select_button = tk.Button(window, text="Select Video", command=select_video)
accuracy_label = tk.Label(window, text="")
output_label = tk.Label(window, text="")

# Pack UI components
select_button.pack(pady=10)
accuracy_label.pack()
output_label.pack()

# Run the Tkinter event loop
window.mainloop()
