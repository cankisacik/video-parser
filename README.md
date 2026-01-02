# video-parser
I created this video parser during my internship so that i can take the required frames for the labeling software quickly and efficently. This Python script automates the process of extracting a specific number of frames from a video file at equal intervals. It is designed for creating image datasets, video summarization, or computer vision preprocessing.

Features
Uniform Sampling: Automatically calculates the frame step based on the total duration to ensure extracted images represent the entire video.

Direct Seeking: Uses CAP_PROP_POS_FRAMES to jump directly to specific frames, making it efficient for long videos.

Automatic Directory Management: Creates the output folder automatically if it doesn't already exist.

Robust Error Handling: Validates video stream integrity and individual frame capture success.

Requirements
The script requires Python and the OpenCV library. You can install the dependency via pip:

Bash

pip install opencv-python
How It Works
The script follows a simple logical flow:

Initialization: Opens the video file and retrieves the total frame count.

Calculation: Divides the total frame count by the desired output number (default is 200) to find the "step" size.

Iteration: Loops through the video, jumping by the calculated step, capturing the frame, and saving it as a high-quality JPEG.

Formatting: Files are saved with a padded naming convention (e.g., ka_00000.jpg, ka_00001.jpg) for easy sorting.

Usage
Set the video_path to your source file.

Set the output_folder to your desired destination.

Run the script:

Python

video_path = "path/to/your/video.mp4"
output_folder = "output_images"

extract_frames(video_path, output_folder)
Configuration
To change the number of frames extracted, update the following two lines in the code:

Step Calculation: Change the denominator in step = max(total_frames // 200, 1).

Break Condition: Change the limit in if saved_count >= 200:.
