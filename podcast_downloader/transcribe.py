"""
This file would be responsible for transcribing the audio from the video to
text using a speech recognition library. Here, functions could be defined to
transcribe the audio of different video formats.
"""
import speech_recognition as sr
from moviepy.video.io.VideoFileClip import VideoFileClip
from copy import deepcopy


class Transcribe:
    def __init__(self, video) -> None:
        self.video = VideoFileClip(video)

    def transcribe(self, **kwargs):
        # Retrieve the audio from the video
        audio = Transcribe.RetrieveAudio.return_audio(
            video=deepcopy(self.video), **kwargs
        )

        # Transcribe the audio using speech recognition
        r = sr.Recognizer()
        with sr.AudioFile(audio) as source:
            text = r.record(source)

        # Print the transcribed text
        return text

    class RetrieveAudio:
        own_video = None

        @classmethod
        def return_audio(cls, video: VideoFileClip, **kwarg) -> bytes:
            # Copy the video used video
            cls.own_video = video

            # Retrieve section of the video if the timer arguments exists
            if "start_time" in kwarg and "end_time" in kwarg:
                cls.__concrete_sections_of_the_video(
                    start_time=kwarg["start_time"], end_time=kwarg["end_time"]
                )

            return cls.own_video.audio

        def __concrete_sections_of_the_video(
            cls, start_time: int, end_time: int
        ) -> str:
            # Extract a concrete section of the video
            return cls.own_video.subclip(start_time, end_time)
