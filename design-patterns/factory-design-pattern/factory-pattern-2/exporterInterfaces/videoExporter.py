from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """ Video Exporter Interface """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def export(self, path):
        """ Add input validation as per use case """
        pass

    @abstractmethod
    def prepare(self, videoData):
        """ Add input validation as per use case """
        pass