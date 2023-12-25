from exporterInterfaces import videoExporter

class LowQVideo(videoExporter.VideoExporter):
    def export(self, path):
        print(f"Exporting video data in LOW quality format to {path}.")

    def prepare(self, videoData):
        print(f"Preparing {videoData} for LOW quality export.")