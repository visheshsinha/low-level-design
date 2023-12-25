from abc import ABC, abstractmethod

class AudioExporter(ABC):
    """ Audio Exporter Interface """
    
    def __init__(self) -> None:
        pass

    @abstractmethod
    def export(self, path):
        """ Add input validation as per use case """
        pass

    @abstractmethod
    def prepare(self, audioData):
        """ Add input validation as per use case """
        pass