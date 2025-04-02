import unittest
import pathlib
import eyed3
from transcriptron import Transcriptor 

class TestTranscriptorMethods(unittest.TestCase):

    def setUp(self):
        self.transcriptor = Transcriptor('testAudio.m4a')

    def tearDown(self):
        converted_file = pathlib.Path('testAudio.wav')
        if converted_file.exists():
            converted_file.unlink('testAudio.wav')
        transcribed_file = pathlib.Path('testAudio.txt')
        if transcribed_file.exists():
            transcribed_file.unlink('testAudio.txt')

    def test_convert_to_wav_should_create_playable_wav(self):
        converted_file = self.transcriptor.convert_to_wav()

        path_to_converted_file = pathlib.Path(converted_file)
        self.assertTrue(path_to_converted_file.exists(), "Converted wav file was not created.")

        loaded_wav = eyed3.load(converted_file)
        self.assertIsNotNone(loaded_wav, "Failed to load wav file.")

    def test_transcribe_should_return_expected_text(self):
        transcripted_filename = self.transcriptor.transcribe()

        path_to_transcripted_file = pathlib.Path(transcripted_filename)
        self.assertTrue(path_to_transcripted_file.exists(), "Transcription file was not created.")

        with open(path_to_transcripted_file) as f:
            content = f.read()
            self.assertIn('Ceci est un test', content, "Transcription did not work properly")

if __name__ == '__main__':
    unittest.main()
