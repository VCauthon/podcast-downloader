"""
This file would act as the command-line interface that accepts the video URL
and important seconds as command-line arguments. Here, functions could be
defined to parse the provided arguments, call the functions defined in the
other files, and display the results to the user.
"""
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
         self._bytes: bytes = None
         self._transcription: str = None
         
         @property
         def title(self):
             return self._title
         
         @title.setter
         def title(self, title: str)
            self._title = title
        
        @staticmethod
        def validate_url(url: str) -> None:
                resultado = urlparse(url)
                return all([resultado.scheme, resultado.netloc])
