from abc import ABC, abstractmethod
from io import BytesIO
from pytube import YouTube


class ContextVideoDownloaded:
    def __init__(self, title: str, bytes: bytes, author: str, seconds: int):
        self.title = title
        self.author = author
        self.seconds = seconds
        self.bytes = bytes


class interface_ABC(ABC):
    @abstractmethod
    def download(self, url) -> ContextVideoDownloaded:
        pass

    @staticmethod
    def detect_platform(url: str) -> str:
        return url.split(".")[1]


class youtube(interface_ABC):
    def download(self, url) -> ContextVideoDownloaded:

        # Create a YouTube object with the video URL
        youtube = YouTube(url)

        # Get the highest resolution video stream available
        stream = youtube.streams.get_highest_resolution()

        # Gets the video into a stream of bytes
        bytes_video = BytesIO()
        stream.stream_to_buffer(bytes_video)

        # Download the video into a stream of bytes
        return ContextVideoDownloaded(
            title=youtube.title,
            author=youtube.author,
            seconds=youtube.length,
            bytes=bytes_video.getvalue(),
        )


class spotify(interface_ABC):
    def download(self, url) -> ContextVideoDownloaded:
        print("spotify")


def downloader(url: str) -> ContextVideoDownloaded:
    # Detects the type of platform
    platform = interface_ABC.detect_platform(url)

    # Raises an error if the platform isn't supported
    available_services = [
        service.__name__ for service in interface_ABC.__subclasses__()
    ]
    if platform not in available_services:
        raise ValueError(
            f'Platform "{platform}" not supported. Available platforms:\
                {available_services}'
        )

    # Returns the download file
    return [
        service
        for service in interface_ABC.__subclasses__()
        if service.__name__ == platform
    ][0]().download(url)


# TODO: Remove this
if __name__ == "__main__":
    downloader("youtube.com")
