from exporterInterfaces import videoExporter

class HighQVideo(videoExporter.VideoExporter):
    def export(self, path):
        print(f"Exporting video data in HIGH quality format to {path}.")

    def prepare(self, videoData):
        print(f"Preparing {videoData} for HIGH quality export.")