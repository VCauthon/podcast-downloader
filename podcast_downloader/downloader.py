"""
This file would contain code for downloading videos from different platforms.
Here, functions could be defined to download the video from a specific
platform and save the video file on the local computer.
"""
from abc import ABC, abstractmethod
from pytube import YouTube


class __interface_ABC(ABC):
    """Interface for downloading videos from different platforms."""

    @abstractmethod
    def download(url):
        pass

    @staticmethod
    def detect_platform(url: str) -> str:
        """Detects the platform of the URL.

        Args:
            url (str): The URL of the video.

        Raises:
            ValueError: If the platform isn't supported.

        Returns:
            str: The platform of the URL.
        """
        if "youtube.com" in url or "youtu.be" in url:
            return "__youtube"
        else:
            raise ValueError("The process could detect the source platform")


class __youtube(__interface_ABC):
    @staticmethod
    def download(url) -> bytes:
        """Downloads a YouTube video.

        Args:
            url (_type_): The URL of the YouTube video.

        Returns:
            bytes: The video file.
        """
        return YouTube(url).streams.get_highest_resolution().stream_to_buffer()


class __spotify(__interface_ABC):
    @staticmethod
    def download(url):
        raise ValueError('Pending implementation')


def downloader(url: str) -> bytes:
    # Detects the type of platform
    platform = __interface_ABC.detect_platform(url)

    # Raises an error if the platform isn't supported
    available_services = [
        service.__name__ for service in __interface_ABC.__subclasses__()
    ]
    if platform not in available_services:
        raise ValueError(
            f'Platform "{platform}" not supported. Available platforms:\
                {available_services}'
        )

    # Returns the download file
    return [
        service
        for service in __interface_ABC.__subclasses__()
        if service.__name__ == platform
    ][0].download(url)


# TODO: Remove this and create a test
# TODO: youtube - There are some videos that can't be downloaded
if __name__ == "__main__":
    downloader("https://www.youtube.com/watch?v=JJYLBzBh4ZI")
