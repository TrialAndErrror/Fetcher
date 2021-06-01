import os
import unittest
import time
from src.video_actions import create_video_object, download_video
from pytube import YouTube
from pathlib import Path

TEST_URLS = [
    'https://youtu.be/papGtuihOfI',
    'https://youtu.be/baPE0CAJjwc',
    'https://youtu.be/6CL21rpJT_E',
    'https://youtu.be/SqqMPaQU-F4',
    'https://youtu.be/ekyY9gpZ6Pg'
]
EXPECTED_NAMES = [
    '[CE1:1] Coding Exercise 1: Section 1 (Introduction)',
    '[CE1:2] Coding Exercise 1: Section 2 (Game Settings)',
    '[CE1:3] Coding Exercise 1: Section 3 (Start Game)',
    '[CE1:4] Coding Exercise 1: Section 4 (Turns and Structure)',
    '[CE1:5] Coding Exercise 1: Section 5 (Troubleshooting)']


class TestVideoActions(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.obj_list = [create_video_object(TEST_URLS[num]) for num in range(5)]
    #
    # @classmethod
    # def tearDown(self) -> None:

    def test_create_video_object(self):
        for num in range(0, 5):
            created_object = self.obj_list[num]
            self.assertIsInstance(created_object, YouTube)
            self.assertTrue(len(created_object.streams) > 0)
            self.assertTrue(created_object.title == EXPECTED_NAMES[num])

    def test_download_video(self):
        for num in range(0, 5):
            path = os.path.join(os.getcwd(), 'tests')
            print(f'Starting download of video {num + 1}')
            download_video(self.obj_list[num], path, audio_only=False)
            print(f'Finished download of video {num + 1}')
            file_exists = os.path.exists(path)
            self.assertTrue(file_exists)
            if file_exists:
                for file in os.listdir(path):
                    os.remove(os.path.join(path, file))
            print(f'Removed video {num + 1}')

            time.sleep(1)

    def test_download_audio_only(self):
        for num in range(0, 5):
            path = str(Path(os.getcwd(), 'tests'))
            print(f'Starting download of video {num + 1}')
            download_video(self.obj_list[num], path, audio_only=True)
            print(f'Finished download of video {num + 1}')
            file_exists = os.path.exists(path)
            self.assertTrue(file_exists)
            if file_exists:
                for file in os.listdir(path):
                    os.remove(os.path.join(path, file))
            print(f'Removed video {num + 1}')

            time.sleep(1)


if __name__ == "__main__":
    unittest.main()
