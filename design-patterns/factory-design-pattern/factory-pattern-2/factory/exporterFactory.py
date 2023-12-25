from abc import ABC, abstractmethod
from exporters.audioExporters import highLevelAudio, midLevelAudio, lowLevelAudio
from exporters.videoExporters import highLevelVideo, midLevelVideo, lowLevelVideo

class ExporterFactory(ABC):
    """ Exporter Factory Interface """
    def __init__(self) -> None:
        pass

    @abstractmethod
    def getExporter(self, quality):
        pass

class GetAudioExporter(ExporterFactory):
    def getExporter(self, quality):
        mapping = {
            'low': lowLevelAudio.LowQAudio(),
            'mid': midLevelAudio.MidQAudio(),
            'high': highLevelAudio.HighQAudio()
        }

        if quality in mapping:
            return mapping[quality]
        
class GetVideoExporter(ExporterFactory):
    def getExporter(self, quality):
        mapping = {
            'low': lowLevelVideo.LowQVideo(),
            'mid': midLevelVideo.MidQVideo(),
            'high': highLevelVideo.HighQVideo()
        }

        if quality in mapping:
            return mapping[quality]