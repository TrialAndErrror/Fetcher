import unittest

from src.video_actions import make_pafy_object

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
