__author__ = 'Xuanli CHEN'
"""
Xuanli Chen
Research Domain: Computer Vision, Machine Learning
Email: xuanli(dot)chen(at)icloud.com
LinkedIn: https://be.linkedin.com/in/xuanlichen
"""
import cv2
import os
import pathlib
from tqdm import tqdm


def extract_frames(video_path: str):
    # Open the video file.
    cap = cv2.VideoCapture(video_path)

    # Get the video file name
    video_name = pathlib.Path(video_path).stem

    # Create a directory with the same name as the video file to save the frames
    output_dir = video_name + '_frames'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Go through the video frame by frame
    frame_num = 0
    while True:
        ret, frame = cap.read()
        # print(frame_num)
        # If we got a frame, save it and go to the next one
        if ret:
            cv2.imwrite(f'{output_dir}/frame{frame_num:04d}.png', frame)
            frame_num += 1
        # If we didn't get a frame, that means we're at the end of the video.
        else:
            break

    # Release the video file
    cap.release()

    print(f"Saved {frame_num} frames to '{output_dir}' directory.")


if __name__ == "__main__":
    video_path = 'movies/GX010232.MOV'  # Enter your video file path here
    extract_frames(video_path)
