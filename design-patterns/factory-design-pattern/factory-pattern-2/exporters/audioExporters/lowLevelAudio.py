from exporterInterfaces import audioExporter

class LowQAudio(audioExporter.AudioExporter):
    def export(self, path):
        print(f"Exporting audio data in LOW quality format to {path}.")

    def prepare(self, audioData):
        print(f"Preparing {audioData} for LOW quality export.")