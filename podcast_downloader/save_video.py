"""
This file would contain code for saving the video on the local computer.
Here, functions could be defined to save the video file to a specific location.
"""
import imageio
import io
import os


# TODO: If this doesn't work try moviepy


def save_video(video: bytes, name_file: str, format: str = '.mp4', path_video: str = None):

    # Loads the stream of bytes into an imageo object
    video_saver = imageio.read(io.BytesIO(video), format=format)

    # Creates the file where the video will be saved
    complete_path = os.path.join(path_video, name_file)
    writer = imageio.get_writer(complete_path)
    for frame in video_saver:
        writer.append_data(frame)

    # Closes the file where the data has been saved
    writer.close()
