import csv
import os
import unittest
from pathlib import Path

from tests import TEST_URLS, EXPECTED_NAMES
from src.tools.debug_tools import clear_youtube_cache


class SingleCsvBasedTest(unittest.TestCase):
    file_path = os.path.join(os.getcwd(), 'test_file.csv')
    output_dir = None

    def setUp(self) -> None:
        clear_youtube_cache()
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
        if self.output_dir:
            for file in os.listdir(self.output_dir):
                os.remove(file)
            os.rmdir(self.output_dir)


def create_multi_csv_data():
    path_1 = Path(os.getcwd(), 'test_csv_1')
    csv_data_1 = [
        [TEST_URLS[0], TEST_URLS[1]],
    ]
    path_2 = Path(os.getcwd(), 'test_csv_2')
    csv_data_2 = [
        [TEST_URLS[2]],
        [TEST_URLS[3]]
    ]
    path_3 = Path(os.getcwd(), 'test_csv_3')
    csv_data_3 = [[TEST_URLS[4]]]
    csv_data = [
        (path_1, csv_data_1),
        (path_2, csv_data_2),
        (path_3, csv_data_3)
    ]
    return csv_data


class MultiCsvBasedTest(unittest.TestCase):
    csv_data = create_multi_csv_data()
    output_dirs = None

    def setUp(self) -> None:
        clear_youtube_cache()
        for data in self.csv_data:
            with open(f'{data[0]}.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data[1])

    def tearDown(self) -> None:
        for data in self.csv_data:
            os.remove(f'{data[0]}.csv')
        if self.output_dirs:
            for folder in self.output_dirs:
                for file in os.listdir(folder):
                    os.remove(Path(folder, file))
                os.rmdir(folder)



