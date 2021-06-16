from math import floor
from typing import Union, AnyStr
from pathlib import Path

import cv2
from PIL import Image

WIDTH = 60
BUCKET = 25
CLIP_FRAMES = 6571
CLIP_LENGTH = 219.0666
# Some magical numbers, but let it be (taken from original bot)
FRAME_LENGTH = 1 / ((floor(CLIP_FRAMES / 4) + 1) / CLIP_LENGTH)*4
ASCII_CHARS = ('⠀', '⠄', '⠆', '⠖', '⠶', '⡶', '⣩', '⣪', '⣫', '⣾', '⣿')
frames_path = Path(__file__).parent / "frames_path"
frames_path.mkdir(exist_ok=True)


def convert_video_to_frames(video_path: Union[AnyStr, Path]) -> None:
    if isinstance(video_path, str):
        video_path = Path(video_path)

        if not video_path.is_file():
            raise FileNotFoundError("Invalid file path")

    video = cv2.VideoCapture(str(video_path))

    success = True
    frame_n = 0
    while success:
        # Reading each frame of video until it fails to be read
        success, image = video.read()
        try:
            cv2.imwrite(str(frames_path / f"frame {frame_n}.png"), image)

        except cv2.error:
            print("Done converting!")
            break

        frame_n += 1

        if frame_n % 100 == 0:
            print(f"{frame_n//100}/65 parts of the video rendered")


def process_image(image: Image) -> AnyStr:
    # Resize image with saving aspect ratio
    width, height = image.size
    aspect_ration = height / width
    resize_height = floor(aspect_ration * WIDTH / 2)
    resize_width = WIDTH
    image = image.resize((resize_width, resize_height))

    # Convert to grayscale
    image = image.convert("L")

    pixels = list(image.getdata())
    # Converting pixels into
    chars_line = [ASCII_CHARS[pixel // BUCKET] for pixel in pixels]
    chars_matrix = []

    # Splitting chars sequence into lines
    for pixel_index in range(0, len(chars_line), WIDTH):
        pixel_stop_index = pixel_index + WIDTH
        chars_matrix.append(''.join(chars_line[pixel_index:pixel_stop_index]))

    return '\n'.join(chars_matrix)
