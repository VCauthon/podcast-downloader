import pytest
from moviepy.video.io.VideoFileClip import VideoFileClip

import sys
sys.path.append('../src')
# TODO: Pending to add the final functions
import podcast_downloader.highlight


@pytest.fixture
def video_file():
    return "video.mp4"


@pytest.fixture
def start_time():
    return 60


@pytest.fixture
def end_time():
    return 120


def test_trim_video(video_file, start_time, end_time):
    # Load the video file
    video = VideoFileClip(video_file)

    # Trim the video
    trimmed_video = trim_video(video, start_time, end_time)

    # Perform assertions to check if the trimming was successful
    assert trimmed_video.duration == end_time - start_time

    # Additional assertions can be added based on your requirements

    # Clean up any temporary files if necessary
