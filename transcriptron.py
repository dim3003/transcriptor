import ffmpeg
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

if __name__ == '__main__':
    transcriptor = Transcriptor('testAudio.m4a')
    transcriptor.convert_to_mp3()
