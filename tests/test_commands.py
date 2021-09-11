from tests.utils import SingleCsvBasedTest, MultiCsvBasedTest
from src.commands import run_single_sheet, run_single_url, run_fetch
from tests import TEST_URLS, EXPECTED_NAMES
import random
import os
from pathlib import Path


class TestSingleUrlCommands(SingleCsvBasedTest):
    def test_run_single_url_audio(self):
        index = random.randint(0, 4)
        audio = True

        output_dir = Path(os.getcwd(), 'Downloads')

        url = TEST_URLS[index]
        name = EXPECTED_NAMES[index]

        run_single_url(url, audio)

        # Assert that the Download directory exists
        self.assertTrue(output_dir.exists())

        # Assert that the file was downloaded
        file_path = Path(output_dir, f'{name}.m4a')
        self.assertTrue(file_path.exists())

        # Remove the file
        os.remove(file_path)

        # Assert that the file was removed
        self.assertFalse(file_path.exists())

    def test_run_single_url_video(self):
        index = random.randint(0, 4)
        audio = False

        output_dir = Path(os.getcwd(), 'Downloads')

        url = TEST_URLS[index]
        name = EXPECTED_NAMES[index]

        run_single_url(url, audio)

        # Assert that the Download directory exists
        self.assertTrue(output_dir.exists())

        # Assert that the file was downloaded
        file_path = Path(output_dir, f'{name}.mp4')
        self.assertTrue(file_path.exists())

        # Remove the file
        os.remove(file_path)

        # Assert that the file was removed
        self.assertFalse(file_path.exists())


class TestSingleSheetCommands(SingleCsvBasedTest):
    def test_run_single_sheet_audio(self):
        audio = True
        self.output_dir = Path(os.getcwd(), 'test_file')
        self.assertFalse(self.output_dir.exists())

        video_count = run_single_sheet(self.file_path, audio)
        self.assertEqual(video_count, 5)

        # Assert that the output directory exists
        self.assertTrue(self.output_dir.exists())

        for name in EXPECTED_NAMES:
            file_path = Path(self.output_dir, f'{name}.m4a')

            # Assert that the file was downloaded
            self.assertTrue(file_path.exists())

            # Remove File
            os.remove(file_path)

            # Assert that the file was removed
            self.assertFalse(file_path.exists())

    def test_run_single_sheet_video(self):
        audio = False
        self.output_dir = Path(os.getcwd(), 'test_file')
        self.assertFalse(self.output_dir.exists())

        video_count = run_single_sheet(self.file_path, audio)
        self.assertEqual(video_count, 5)

        # Assert that the output directory exists
        self.assertTrue(self.output_dir.exists())

        for name in EXPECTED_NAMES:
            file_path = Path(self.output_dir, f'{name}.mp4')

            # Assert that the file was downloaded
            self.assertTrue(file_path.exists())

            # Remove File
            os.remove(file_path)

            # Assert that the file was removed
            self.assertFalse(file_path.exists())


class TestFetchCommands(MultiCsvBasedTest):
    def test_run_fetch_audio(self):
        audio = True
        self.output_dirs = []

        for data in self.csv_data:
            output_dir = data[0]
            self.output_dirs.append(output_dir)
            self.assertFalse(output_dir.exists())

        video_count = run_fetch(audio)
        self.assertEqual(video_count, 5)

        # Assert that the output directory exists
        for num in range(3):
            output_dir = self.csv_data[num][0]
            self.assertTrue(output_dir.exists())

        # Assert that each file exists
        for index, name in enumerate(EXPECTED_NAMES):
            if index < 2:
                output_dir = self.csv_data[0][0]
            elif index < 4:
                output_dir = self.csv_data[1][0]
            else:
                output_dir = self.csv_data[2][0]

            file_path = Path(output_dir, f'{name}.m4a')

            # Assert that the file was downloaded
            self.assertTrue(file_path.exists())

        #     # Remove File
        #     os.remove(file_path)
        #
        #     # Assert that the file was removed
        #     self.assertFalse(file_path.exists())
        #
        # for num in range(3):
        #     output_dir = self.csv_data[num][0]
        #     os.rmdir(output_dir)
        #     self.assertFalse(output_dir.exists())

    def test_run_fetch_video(self):
        audio = False
        self.output_dirs = []

        for data in self.csv_data:
            output_dir = data[0]
            self.output_dirs.append(output_dir)
            self.assertFalse(output_dir.exists())

        video_count = run_fetch(audio)
        self.assertEqual(video_count, 5)

        # Assert that the output directory exists
        for num in range(3):
            output_dir = self.csv_data[num][0]
            self.assertTrue(output_dir.exists())

        # Assert that each file exists
        for index, name in enumerate(EXPECTED_NAMES):
            if index < 2:
                output_dir = self.csv_data[0][0]
            elif index < 4:
                output_dir = self.csv_data[1][0]
            else:
                output_dir = self.csv_data[2][0]

            file_path = Path(output_dir, f'{name}.mp4')

            # Assert that the file was downloaded
            self.assertTrue(file_path.exists())

        #     # Remove File
        #     os.remove(file_path)
        #
        #     # Assert that the file was removed
        #     self.assertFalse(file_path.exists())
        #
        # for num in range(3):
        #     output_dir = self.csv_data[num][0]
        #     os.rmdir(output_dir)
        #     self.assertFalse(output_dir.exists())
