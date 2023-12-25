from factory import exporterFactory
from exporterInterfaces import audioExporter, videoExporter

class MediaExporter:
    def __init__(self) -> None:
        self.qualities = ['low', 'mid', 'high']
        self.path = "/usr/tmp/video"
        self.getAudioExporter = exporterFactory.GetAudioExporter()
        self.getVideoExporter = exporterFactory.GetVideoExporter()

    def executeExporting(self):
        audioExportQuality = input(
            f"Enter desired output audio quality ({', '.join(self.qualities)}): "
        )
        videoExportQuality = input(
            f"Enter desired output video quality ({', '.join(self.qualities)}): "
        )

        audioExportObject = self.getAudioExporter.getExporter(audioExportQuality)
        if isinstance(audioExportObject, audioExporter.AudioExporter):
            audioExportObject.prepare(audioData = 'audio data') # can add data validation as & when req.
        else:
            raise Exception(f'Unkown audio quality type: {audioExportQuality}')
        
        videoExportObject = self.getVideoExporter.getExporter(videoExportQuality)
        if isinstance(videoExportObject, videoExporter.VideoExporter):
            videoExportObject.prepare(videoData = 'video data') # can add data validation as & when req.
        else:
            raise Exception(f'Unkown audio quality type: {videoExportObject}')
        
        print('Media Export completed successfully')

if __name__ == '__main__':
    mediaExportObject = MediaExporter()
    mediaExportObject.executeExporting()