import cv2
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Video format not supported")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames of your video is {total_frames}")

    step = max(total_frames // 200, 1) "Change the maximum frame number here for the desired frame parse"
    print(f"A frame will be taken for every {step} frame")

    os.makedirs(output_folder, exist_ok=True)

    saved_count = 0
    for i in range(0, total_frames, step):
        if saved_count >= 200: "Also change the frame number from here aswell"
            break
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if not ret:
            print(f"Cannot take frame {i}")
            continue
        filename = f"ka_{saved_count:05d}.jpg"
        filepath = os.path.join(output_folder, filename)
        saved = cv2.imwrite(filepath, frame)
        if not saved:
            print(f"Cannot save {filename}")
        saved_count += 1

    cap.release()
    print(f"Saved {saved_count} frames to {output_folder}")
    
video_path = "path to your video"
output_folder = "path to the desired output folder"

extract_frames(video_path, output_folder)
