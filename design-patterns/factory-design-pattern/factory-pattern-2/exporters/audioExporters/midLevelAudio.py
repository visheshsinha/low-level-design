from exporterInterfaces import audioExporter

class MidQAudio(audioExporter.AudioExporter):
    def export(self, path):
        print(f"Exporting audio data in MID quality format to {path}.")

    def prepare(self, audioData):
        print(f"Preparing {audioData} for MID quality export.")