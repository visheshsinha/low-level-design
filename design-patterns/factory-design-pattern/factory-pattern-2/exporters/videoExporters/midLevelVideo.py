from exporterInterfaces import videoExporter

class MidQVideo(videoExporter.VideoExporter):
    def export(self, path):
        print(f"Exporting video data in MID quality format to {path}.")

    def prepare(self, videoData):
        print(f"Preparing {videoData} for MID quality export.")