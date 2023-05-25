"""
This file would be responsible for transcribing the audio from the video to
text using a speech recognition library. Here, functions could be defined to
transcribe the audio of different video formats.
"""
import speech_recognition as sr
from moviepy.editor import VideoFileClip
import io


class Transcribe:
    def __init__(self, video: bytes) -> None:
        self.video = VideoFileClip(video)

    def transcribe(self, **kwargs):

        # Retrieve the audio from the video
        audio = self.__return_audio(**kwargs)

        # Transcribe the audio using speech recognition
        r = sr.Recognizer()
        with sr.AudioFile(io.BytesIO(audio)) as source:
            text = r.record(source)

        # Print the transcribed text
        return text

    def __return_audio(self, **kwarg) -> bytes:

        # Retrieves the audio from the video
        audio = self.video.subclip(
            kwarg["start_time"], kwarg["end_time"]).audio\
                if "start_time" in kwarg and "end_time" in kwarg \
                else self.video.audio

        # Returns the audio
        return audio.to_soundarray().tobytes()
