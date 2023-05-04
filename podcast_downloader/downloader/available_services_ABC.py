from abc import ABC, abstractmethod


class ServicesABC(ABC):
    @abstractmethod
    def download(self, url):
        pass
