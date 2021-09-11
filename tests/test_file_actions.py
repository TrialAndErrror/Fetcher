import os
import unittest
from tests import TEST_URLS
import csv


from src.file_actions import find_files, find_youtube_links, find_links, get_link_entry_list


class TestFileActions(unittest.TestCase):
    file_path = os.path.join(os.getcwd(), 'test_file.csv')

    def setUp(self) -> None:
        csv_data = [
            [TEST_URLS[0], TEST_URLS[1]],
            [TEST_URLS[2], TEST_URLS[3]],
            [TEST_URLS[4]]
        ]

        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

    def tearDown(self) -> None:
        os.remove(self.file_path)

    def test_find_files(self):
        files_found, files_list = find_files()

        self.assertTrue(files_found)
        self.assertGreater(len(files_list), 0)
        self.assertIn('test_file.csv', files_list)

    def test_find_youtube_links(self):
        video_files = find_youtube_links(self.file_path)

        self.assertEqual(len(video_files), 5)
        for url in TEST_URLS:
            self.assertIn(url, video_files)

    def test_get_link_entry_list(self):
        with open(self.file_path) as file:
            entry_list = get_link_entry_list(file)

        self.assertEqual(len(entry_list), 5)
        for url in TEST_URLS:
            self.assertIn(url, entry_list)

    def test_find_links(self):
        output_dir, urls = find_links(self.file_path)

        self.assertEqual(output_dir, f'{os.path.join(os.getcwd(), "test_file")}/')

        self.assertEqual(len(urls), 5)
        for url in TEST_URLS:
            self.assertIn(url, urls)
