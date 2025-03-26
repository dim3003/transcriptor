import unittest
import pathlib
import eyed3
from transcriptron import Transcriptor 

class TestTranscriptorMethods(unittest.TestCase):
    def setUp(self):
        self.transcriptor = Transcriptor('testAudio.m4a')

    def tearDown(self):
        converted_file = pathlib.Path('testAudio.mp3')
        if converted_file.exists():
            converted_file.unlink('testAudio.mp3')

    def test_convert_to_mp3_should_create_playable_mp3(self):
        converted_file = self.transcriptor.convert_to_mp3()
        path_to_converted_file = pathlib.Path(converted_file)
        self.assertTrue(path_to_converted_file.exists(), "Converted MP3 file was not created.")
        loaded_mp3 = eyed3.load(converted_file)
        self.assertIsNotNone(loaded_mp3, "Failed to load MP3 file.")

if __name__ == '__main__':
    unittest.main()
