# Video Processing Project Setup Guide

## Clone the Project Repository

Clone the project repository to your local machine using Git.

## Install Python

Ensure that you have Python 3.x installed on your machine. You can check by running:

python --version

## Install Required Libraries

Install the required libraries by running the following command:

pip install opencv-python mediapipe

## Navigate to Project Directory

Open a terminal or command prompt and navigate to the directory where the project is cloned.

## Run the Script

Navigate to the directory containing the `video_processor.py` file in your terminal or command prompt. Run the script using the following command:

python video_processor.py

## Process Video

The "Video Processing" window will appear. Click the "Select Video" button to choose a video file (supported format: `.mp4`). The script will start processing the selected video, displaying the processed video with detected landmarks.

## View Accuracy

While processing, the accuracy label will display a random accuracy value.

## Save Processed Video

Once processing is complete, the processed video will be saved in the same directory as the original video file with the suffix "\_processed.avi". The output label will display the path where the processed video is saved.

## Close Application

You can close the application window by clicking the close button (X) on the window title bar or by pressing the close button of the operating system window manager.
