"""
This file would act as the command-line interface that accepts the video URL
and important seconds as command-line arguments. Here, functions could be
defined to parse the provided arguments, call the functions defined in the
other files, and display the results to the user.
"""
from typing import List, Tuple
from urllib.parse import urlparse


class Download:
    def __init__(self, url: str):
        # Raises an error if the url isn't valid
        self.url: str = url
        self.validate_url(self.url)

        # Initialize the rest of the variables
        self._title: str = None
        self._author: str = None
        self._seconds: int = None
        self._chapters: List[Tuple[int, int]] = None
        self._stream_video: bytes = None
        self._transcription: str = None

    @staticmethod
    def validate_url(url: str) -> None:
        resultado = urlparse(url)
        return all([resultado.scheme, resultado.netloc])

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str) -> None:
        self._author = author

    @property
    def seconds(self) -> str:
        hours, remainder = divmod(self._seconds, 3600)
        minutes, seconds = divmod(self._seconds, 60)

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    @seconds.setter
    def seconds(self, seconds: int) -> None:
        self._seconds = seconds

    @property
    def chapters(self) -> List[Tuple[int, int]]:
        return self._chapters

    @chapters.setter
    def chapters(self, chapter: Tuple[int, int]) -> None:
        if self._chapters is None:
            self._chapters = []
        self._chapters.append(chapter)

    @property
    def stream_video(self) -> str:
        return self._stream_video

    @stream_video.setter
    def stream_video(self, stream: bytes) -> None:
        self._stream_video = stream

    @property
    def transcription(self) -> str:
        return self._transcription

    @transcription.setter
    def transcription(self, transcription: str) -> None:
        self._transcription = transcription


"""

comand line

url - minuts:minuts,... - output site (optional)

retrive from file

csv - output site (optional)

download
highlight
  resume
transcribe
save

"""
