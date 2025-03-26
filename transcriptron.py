import ffmpeg
import whisper 
from pathlib import Path

class Transcriptor:

    def __init__(self, filename):
        self.filename = filename
        self.mp3_filename = None

    def convert_to_mp3(self):
        try:
            original_path = Path(self.filename)
            self.mp3_filename = str(original_path.with_suffix('.mp3'))
            ffmpeg.input(original_path).output(self.mp3_filename, loglevel="quiet").run()
            return self.mp3_filename 

        except ffmpeg.Error as e:
            print(f"An error occurred: {e}")

    def transcribe(self):
        self.convert_to_mp3()
        original_path = Path(self.filename)
        txt_filename = str(original_path.with_suffix('.txt'))

        model = whisper.load_model("large")
        result = model.transcribe(self.mp3_filename, language="fr")

        with open(txt_filename, 'w') as file:
            file.write(result["text"])
        return txt_filename

if __name__ == '__main__':
    #print(whisperx.available_models())
    transcriptor = Transcriptor('testAudio.m4a')
    transcriptor.transcribe()
