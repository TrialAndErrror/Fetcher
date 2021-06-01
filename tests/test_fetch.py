from unittest import TestCase
from src.fetch import read_spreadsheet
import csv
import os
from pathlib import Path


class TestReadSpreadsheet(TestCase):
	def setUp(self) -> None:
		sample_sheet = [
			["not a link", "also not a link", "https://www.google.com"],
			["https://www.youtube.com/watch?v=h828fACU9ik", "TnE 100 Days of Talking Episode 1", "description"],
			["Misshapen data", "https://www.youtube.com/watch?v=SG2UpSHZgi0"],
			["Nothing to see here..."]
		]

		self.test_filename = 'sample_sheet.csv'

		with open(self.test_filename, 'w+') as file:
			writer = csv.writer(file)
			for line in sample_sheet:
				writer.writerow(line)

	def tearDown(self) -> None:
		os.remove('sample_sheet.csv')

	def test_read_spreadsheet(self) -> None:
		test_output_dir, test_video_files = read_spreadsheet(self.test_filename)

		self.assertEqual(Path(test_output_dir), Path('sample_sheet'))

		self.assertIsNotNone(test_video_files)

		self.assertIsInstance(test_video_files, list)

		self.assertTrue(len(test_video_files) == 2)
		
		for item in ['https://www.youtube.com/watch?v=h828fACU9ik', 'https://www.youtube.com/watch?v=SG2UpSHZgi0']:
			self.assertIn(item, test_video_files)

		self.assertNotIn('https://www.google.com', test_video_files)



