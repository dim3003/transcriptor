import ffmpeg
import sys
import whisper
from pathlib import Path


class Transcriptor:

    def __init__(self, filename):
        self.filename = filename
        self.wav_filename = None

    def convert_to_wav(self):
        try:
            original_path = Path(self.filename)
            self.wav_filename = str(original_path.with_suffix('.wav'))
            ffmpeg.input(original_path).output(
                self.wav_filename, loglevel="quiet").run()
            return self.wav_filename

        except ffmpeg.Error as e:
            print(f"An error occurred: {e}")

    def transcribe(self):
        self.convert_to_wav()
        original_path = Path(self.filename)
        txt_filename = str(original_path.with_suffix('.txt'))

        model = whisper.load_model("large")
        result = model.transcribe(self.wav_filename, language="fr")

        with open(txt_filename, 'w') as file:
            file.write(result["text"])
        return txt_filename


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    transcriptor = Transcriptor(audio_file)
    transcriptor.transcribe()
