from exporterInterfaces import audioExporter

class HighQAudio(audioExporter.AudioExporter):
    def export(self, path):
        print(f"Exporting audio data in HIGH quality format to {path}.")

    def prepare(self, audioData):
        print(f"Preparing {audioData} for HIGH quality export.")