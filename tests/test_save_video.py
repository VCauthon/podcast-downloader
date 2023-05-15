import pytest
import os
import imageio

import sys
sys.path.append('../src')
from podcast_downloader.save_video import save_video  # noqa: E402


@pytest.fixture
def video_data():
    # Create a sample video data
    video = b'\x00\x01\x02\x03\x04'  # Sample video bytes
    name_file = 'test_video'
    format = '.mp4'
    path_video = 'test_videos'
    
    return video, name_file, format, path_video

def test_save_video(tmpdir, video_data):
    # Create a temporary directory for testing
    temp_dir = tmpdir.mkdir('test_save_video')
    path_video = str(temp_dir)
    
    # Call the save_video function
    video, name_file, format, _ = video_data
    save_video(video, name_file, format, path_video)
    
    # Check if the video file exists in the specified path
    video_path = os.path.join(path_video, name_file + format)
    assert os.path.isfile(video_path)
    
    # Check if the saved video file is readable
    saved_video = imageio.imread(video_path)
    assert isinstance(saved_video, imageio.core.util.Array)


