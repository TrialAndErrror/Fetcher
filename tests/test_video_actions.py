import unittest

from src.video_actions import make_pafy_object
from tests import TEST_URLS, EXPECTED_NAMES


class TestVideoActions(unittest.TestCase):
    def test_make_pafy_object_video(self):
        for num in range(0, 5):
            url = TEST_URLS[num]
            name = EXPECTED_NAMES[num]

            video_stream = make_pafy_object(url, False)

            self.assertTrue(video_stream.title == name)
            self.assertTrue(video_stream.mediatype == 'normal')
            self.assertTrue(video_stream.extension == 'mp4')

    def test_make_pafy_object_audio(self):
        for num in range(0, 5):
            url = TEST_URLS[num]
            name = EXPECTED_NAMES[num]

            video_stream = make_pafy_object(url, True)

            self.assertTrue(video_stream.title == name)
            self.assertTrue(video_stream.mediatype == 'audio')
            self.assertTrue(video_stream.extension == 'm4a')


if __name__ == "__main__":
    unittest.main()
