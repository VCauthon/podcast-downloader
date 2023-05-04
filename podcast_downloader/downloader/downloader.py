from abc import ABC, abstractmethod


class interface_ABC(ABC):
    @abstractmethod
    def download(self, url):
        pass

    @staticmethod
    def detect_platform(url: str) -> str:
        return 'url.split(".")[1]'


class youtube(interface_ABC):
    def download(self, url):
        print("youtube")


class spotify(interface_ABC):
    def download(self, url):
        print("spotify")


def downloader(url: str) -> bytes:
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


downloader("youtube.com")
