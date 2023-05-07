"""
This file would be responsible for highlighting the most important seconds of
the video. Here, functions could be defined to highlight key moments of a video
based on the minutes and seconds provided by the user.
"""

from moviepy.video.io.VideoFileClip import VideoFileClip

# Specify the video file name
video_file = "video.mp4"

# Specify the start and end times in seconds
start_time = 60  # start at minute 1
end_time = 120  # end at minute 2

# Load the video file
video = VideoFileClip(video_file)

# Trim the video
video = video.subclip(start_time, end_time)

# Write the trimmed video to a new file
video.write_videofile("trimmed_video.mp4")
