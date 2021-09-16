import os
import unittest
from tests import TEST_URLS
from tests.utils import SingleCsvBasedTest


from src.file_actions import find_files, find_youtube_links, find_links, get_link_entry_list


class TestFileActions(SingleCsvBasedTest):
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
